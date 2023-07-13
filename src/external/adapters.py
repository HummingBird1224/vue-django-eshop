from allauth.socialaccount.adapter import DefaultSocialAccountAdapter
from allauth.utils import get_user_model
from allauth.account.utils import user_email, user_field
from allauth.utils import valid_email_or_none


class SocialAccountAdapter(DefaultSocialAccountAdapter):

    def pre_social_login(self, request, sociallogin):
        user = sociallogin.user
        if user.id:
            return
        if not user.email:
            return
        try:
            user = get_user_model().objects.get(email=user.email)
            sociallogin.connect(request, user)
        except get_user_model().DoesNotExist:
            pass

    def populate_user(self,
                      request,
                      sociallogin,
                      data):
        email = data.get('email')
        name = data.get('name')
        company_name = data.get('company_name')
        url = data.get('url')
        user = sociallogin.user
        user_email(user, valid_email_or_none(email) or '')
        user_field(user, 'name', name)
        user_field(user, 'company_name', company_name)
        user_field(user, 'url', url)
        return user

    def is_open_for_signup(self, request, sociallogin):
        return True
