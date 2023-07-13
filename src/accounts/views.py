from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.messages.views import SuccessMessageMixin
from django.core.exceptions import ObjectDoesNotExist
from django.db import transaction
from django.http import Http404
from django.views.generic.base import TemplateView
from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy
from django.utils import timezone
from django.utils.decorators import method_decorator
from django.utils.translation import gettext as _
from allauth.account import signals
from allauth.account.models import EmailAddress, EmailConfirmation
from allauth.account.utils import user_pk_to_url_str
from allauth.account.views import LoginView, ConfirmEmailView, PasswordChangeView
from allauth.exceptions import ImmediateHttpResponse
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import DeliveryAddress, PayJPInfo, BillingAddress
from .forms import SignupForm, DeliveryAddressCreationForm, BillingAddressCreationForm
from .adapter import get_adapter
from utils.payjp_functions import (payjp_change_default_card,
                                   payjp_get_default_card,
                                   payjp_get_customer_cards,
                                   payjp_create_card,
                                   payjp_delete_card)
from carts.models import Cart
from orders.models import Order
import logging


logger = logging.getLogger(__name__)
User = get_user_model()


class CustomLoginView(LoginView):
    """ログイン
    カートのマージ
    orderの引き継ぎ
    """

    def form_valid(self, form):
        success_url = self.get_success_url()
        try:
            # DATA BEFORE LOGIN
            anonymous_cart = Cart.objects.get_from_request(self.request)
            anonymous_order = Order.objects.clear_order(self.request)

            # LOGIN
            ret = form.login(self.request, redirect_url=success_url)

            # AUTHENTICATED USER'S CART
            Cart.objects.clear_cart(self.request)
            authenticated_cart = Cart.objects.get_from_request(self.request)

            # MERGE CARTS
            if anonymous_cart and authenticated_cart and anonymous_cart != authenticated_cart:
                authenticated_cart.merge_with(anonymous_cart)

            # SET CURRENT ORDER
            if anonymous_order:
                Order.objects.set_current_order(self.request, anonymous_order)

            if self.request.user.is_authenticated:
                logger.info("User login {}:{}.".format(self.request.user.email, self.request.user.name))
            return ret
        except ImmediateHttpResponse as e:
            logger.error("User login failed.")
            return e.response


class CustomPasswordChangeView(PasswordChangeView):

    success_url = reverse_lazy('account_change_password')


class ConfirmEmailWithRedirectionView(ConfirmEmailView):
    """アカウント作成確認メールの確認
    確認後ログイン
    カートのマージ
    orderの引き継ぎ
    """

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["redirect_field_name"] = "next"
        context["redirect_field_value"] = self.request.GET.get("next")
        return context

    def get_redirect_url(self):
        return get_adapter(self.request).get_email_confirmation_redirect_url(self.request)

    def post(self, *args, **kwargs):
        # DATA BEFORE LOGIN
        anonymous_cart = Cart.objects.get_from_request(self.request)
        anonymous_order = Order.objects.clear_order(self.request)

        # LOGIN ACTION OCCURS HERE WITH SESSION FLUSHING
        ret = super().post(*args, **kwargs)

        # AUTHENTICATED USER'S CART
        Cart.objects.clear_cart(self.request)
        authenticated_cart = Cart.objects.get_from_request(self.request)

        # MERGE CARTS
        if anonymous_cart and authenticated_cart and anonymous_cart != authenticated_cart:
            authenticated_cart.merge_with(anonymous_cart)

        # SET CURRENT ORDER
        if anonymous_order:
            Order.objects.set_current_order(self.request, anonymous_order)

        if self.request.user.is_authenticated:
            logger.info("Email confirmed {}:{}.".format(self.request.user.email, self.request.user.name))
        return ret


class SignUpAPIView(APIView):
    """決済画面でのユーザー登録
    ログインしていなくても許可

    POST PARAMS:
    - oid: order id
    """

    permission_classes = [AllowAny, ]

    def post(self, request, format=None):
        adapter = get_adapter(request)
        # BLOCK AUTHENTICATED USER
        if request.user.is_authenticated:
            return Response({'message': 'User already logged in.'}, status=status.HTTP_400_BAD_REQUEST)
        # CHECK IF THE POSTED ID IS THE RIGHT ONE
        try:
            ref_code = request.data.get("oid")
            order = Order.objects.get(ref_code=ref_code)
            current_order = Order.objects.get_current_order(request)
            if not current_order or order != current_order:
                logger.warning("Requested order invalid. ref:{}.".format(ref_code))
                return Response({'message': 'Accessing wrong order'}, status=status.HTTP_400_BAD_REQUEST)
        except ObjectDoesNotExist:
            logger.warning("Requested order invalid.")
            return Response({'message': 'Accessing wrong order.'}, status=status.HTTP_400_BAD_REQUEST)
        # FORM VALIDATION
        form = SignupForm(request.data)
        if form.is_valid():
            # USER CREATION
            user = form.save(self.request)
            signals.user_signed_up.send(sender=user.__class__,
                                        request=request,
                                        user=user)

            # SET ORDER OWNER TO THE NEWLY CREATED USER
            order.user = user
            order.save()

            # ALLAUTH EMAIL DATA (NOT SUPPOSE TO HAVE VERIFIED EMAIL)
            has_verified_email = EmailAddress.objects.filter(user=user,
                                                             verified=True).exists()
            if not has_verified_email:
                redirect_to = order.get_billing_url()
                self.send_email_confirmation(request, user, adapter, signup=True, redirect_to=redirect_to)
                adapter.login(request, user)
                signals.user_logged_in.send(sender=user.__class__,
                                            request=request,
                                            user=user)
                return Response({"message": "success."}, status=status.HTTP_200_OK)
            logger.error("User already has verified email.".format())
            return Response({'message': "Something went wrong."}, status=status.HTTP_400_BAD_REQUEST)
        # RETURN MESSAGES FOR INVALID FIELDS
        logger.info("Invalid signup form sent from billing view.")
        return Response({'message': "Form incomplete.",
                         'errors': dict(form.errors.items())}, status=status.HTTP_400_BAD_REQUEST)

    def send_email_confirmation(self, request, user, adapter, signup=True, redirect_to=None):
        email = user.email
        try:
            email_address = EmailAddress.objects.get_for_user(user, email)
            if not email_address.verified:
                confirmation = EmailConfirmation.create(email_address)
                # SEND CONFIRMATION MAIL WITH REDIRECT URL
                adapter.send_confirmation_mail(request, confirmation,
                                                            signup, redirect_to=redirect_to)
                confirmation.sent = timezone.now()
                confirmation.save()
                signals.email_confirmation_sent.send(sender=confirmation.__class__,
                                                     request=request,
                                                     confirmation=confirmation,
                                                     signup=signup)
                logger.info("Verification email resent from billing view.")
        except EmailAddress.DoesNotExist:
            email_address, created = EmailAddress.objects.get_or_create(
                user=user, email__iexact=email, defaults={"email": email}
            )
            if created:
                confirmation = EmailConfirmation.create(email_address)
                # SEND CONFIRMATION MAIL WITH REDIRECT URL
                adapter.send_confirmation_mail(request, confirmation, signup,
                                                            redirect_to=redirect_to)
                confirmation.sent = timezone.now()
                confirmation.save()
                signals.email_confirmation_sent.send(sender=confirmation.__class__,
                                                     request=request,
                                                     confirmation=confirmation,
                                                     signup=signup)
                logger.info("Verification email sent from billing view.")
            assert email_address
        if signup:
            adapter.stash_user(request, user_pk_to_url_str(user))


@method_decorator(login_required, name='dispatch')
class AccountUpdateView(SuccessMessageMixin, UpdateView):

    template_name = 'accounts/account_update.html'
    model = User
    fields = ['company_name', 'name', 'url', 'email']
    success_url = reverse_lazy('account_update')
    success_message = '情報が更新されました。'

    def get_object(self, queryset=None):
        if queryset is None:
            queryset = self.get_queryset()
        pk = self.request.user.id
        if pk is not None:
            queryset = queryset.filter(pk=pk)
        if pk is None:
            raise AttributeError(
                "Generic detail view %s must be called with either an object "
                "pk or a slug in the URLconf." % self.__class__.__name__
            )
        try:
            obj = queryset.get()
        except queryset.model.DoesNotExist:
            logger.info("User does not exist with pk:{}.".format(pk))
            raise Http404(_("No %(verbose_name)s found matching the query") %
                          {'verbose_name': queryset.model._meta.verbose_name})
        return obj

    def form_valid(self, form):
        # TODO: 確認メール送るかどうか議論
        res = super().form_valid(form)
        new_email = form.cleaned_data.get('email')
        user = self.get_object()
        ea = EmailAddress.objects.filter(user=user).first()
        with transaction.atomic():
            user.email = new_email
            user.save()
            ea.email = new_email
            ea.verified = True
            ea.save()
        return res


@method_decorator(login_required, name='dispatch')
class CreditManageView(TemplateView):

    template_name = 'accounts/credit_manage.html'


@method_decorator(login_required, name='dispatch')
class AddressManageView(TemplateView):

    template_name = 'accounts/address_manage.html'


class AccountCreditListAPIView(APIView):

    def get(self, request, format=None, *args, **kwargs):
        user = request.user
        if not user.has_payjp_customer():
            return Response({}, status=status.HTTP_400_BAD_REQUEST)
        customer_id = user.payjpinfo.customer_id
        res = payjp_get_customer_cards(customer_id)
        defaulut_card = payjp_get_default_card(customer_id)
        for _ in res:
            if _['id'] == defaulut_card:
                _['is_default'] = True
            else:
                _['is_default'] = False
        return Response({"cards": res}, status=status.HTTP_200_OK)


class AccountCreditCreateAPIView(APIView):

    def post(self, request, format=None, *args, **kwargs):
        data = request.data
        token = data["token"]
        user = request.user
        customer_id = user.payjpinfo.customer_id
        res = payjp_create_card(customer_id, token)
        return Response({"card_id": res}, status=status.HTTP_200_OK)


class AccountCreditDeleteAPIView(APIView):

    def post(self, request, format=None, *args, **kwargs):
        data = request.data
        card_id = data["id"]
        user = request.user
        customer_id = user.payjpinfo.customer_id
        payjp_delete_card(customer_id, card_id)
        return Response({"card_id": card_id}, status=status.HTTP_200_OK)


class AccountCreditChangeDefaultAPIView(APIView):

    def post(self, request, format=None, *args, **kwargs):
        data = request.data
        card_id = data["id"]
        user = request.user
        customer_id = user.payjpinfo.customer_id
        payjp_change_default_card(customer_id, card_id)
        return Response({"card_id": card_id}, status=status.HTTP_200_OK)


class AccountAddressListAPIView(APIView):

    def get(self, request, format=None, *args, **kwargs):
        addresses = []
        user = request.user
        for a in user.deliveryaddress_set.all():
            addresses.append({
                "name": a.name,
                "postal_code": a.postal_code,
                "address": a.get_full_address(),
                "tel": a.tel,
                "is_default": a.is_default,
                "id": a.id
            })
        return Response({"addresses": addresses}, status=status.HTTP_200_OK)


class AccountAddressCreateAPIView(APIView):

    def post(self, request, format=None, *args, **kwargs):
        user = request.user
        data = request.data
        data['user'] = user.id
        form = DeliveryAddressCreationForm(data)
        if form.is_valid():
            address = form.save()
            b_address = BillingAddressCreationForm(data).save()
            user.change_default_delivery_address(address)
            user.change_default_billing_address(b_address)
            res = {
                "name": address.name,
                "postal_code": address.postal_code,
                "address": address.get_full_address(),
                "tel": address.tel,
                "id": address.id
            }
            return Response(res, status=status.HTTP_200_OK)
        return Response({"errors": form.errors}, status=status.HTTP_400_BAD_REQUEST)


class AccountAddressDeleteAPIView(APIView):

    def post(self, request, format=None, *args, **kwargs):
        user = request.user
        data = request.data
        id = data["id"]
        address = user.deliveryaddress_set.filter(id=id).first()
        if address:
            address.delete()
            ba = BillingAddress.objects.filter(
                name=address.name,
                postal_code=address.postal_code,
                prefecture=address.prefecture,
                city=address.city,
                building=address.building,
                tel=address.tel
            ).first()
            if ba:
                ba.delete()
        return Response({"id": id}, status=status.HTTP_200_OK)


class AccountAddressChangeDefaultAPIView(APIView):

    def post(self, request, format=None, *args, **kwargs):
        user = request.user
        data = request.data
        id = data["id"]
        address = user.deliveryaddress_set.filter(id=id).first()
        if address:
            user.change_default_delivery_address(address)
            ba = BillingAddress.objects.filter(
                name=address.name,
                postal_code=address.postal_code,
                prefecture=address.prefecture,
                city=address.city,
                building=address.building,
                tel=address.tel
            ).first()
            if ba:
                user.change_default_billing_address(ba)
        return Response({"id": id}, status=status.HTTP_200_OK)


@method_decorator(login_required, name='dispatch')
class MyDesignView(TemplateView):

    template_name = 'accounts/mydesign.html'
