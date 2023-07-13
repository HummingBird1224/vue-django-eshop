from django.conf import settings
from django.contrib import messages
from django.http import Http404
from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from django.shortcuts import get_object_or_404, redirect
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.generics import RetrieveAPIView, ListAPIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from .models import (Product,
                     ProductCategory,
                     ProductUsecase)
from .serializers import ProductSerializer, ProductCategoryWithChildrenSerializer
from .extras.cardboard_colors import cardboard_colors
from math import ceil


class ProductDetailView(DetailView):
    """商品詳細ページ
    カテゴリごとにテンプレートの切り替え
    """
    related_products_num = 3
    template_name = 'products/product_detail.html'

    def get_object(self, *args, **kwargs):
        slug = self.kwargs.get('slug', None)
        obj = get_object_or_404(Product, slug=slug)
        # EXCLUDE EXTERNAL PRODUCTS
        if obj.category.get_parent_or_self().slug == 'external':
            raise Http404()
        obj.parent_category = obj.category.get_parent_or_self()
        return obj

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['static_url'] = settings.STATIC_URL

        # 関連商品同じジャンルの中からランダムで三つ
        context['related_products'] = self.get_related_products()
        return context

    def get_related_products(self):
        products = Product.objects.filter(category=self.object.category).exclude(slug=self.object.slug)
        return products.order_by('?')[:self.related_products_num]


class ProductListView(TemplateView):
    """商品一覧
    カテゴリとユースケースがある
    """

    template_name = 'products/product_list.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        slug = kwargs.get('slug')
        category_root = get_object_or_404(ProductCategory, slug='root')
        context['categories'] = ProductCategory.objects.public().filter(parent_category=category_root)
        context['usecases'] = ProductUsecase.objects.all()

        # CATEGORY
        category = ProductCategory.objects.filter(slug=slug).first()
        if category:
            # EXCLUDE EXTERNALS
            if category.get_parent_or_self().slug == 'external':
                raise Http404()
            context['category'] = category
            context['parent_category'] = category.get_parent_or_self()
            context['is_usecase'] = False
            return context

        # USECASE
        usecase = ProductUsecase.objects.filter(slug=slug).first()
        if usecase:
            data = []
            for cat in ProductCategory.objects.public().filter(parent_category=category_root):
                products = Product.objects.in_category(cat).filter(usecase=usecase)
                if products:
                    data.append({'category': cat.name, 'products': products})
            context['usecase'] = usecase.name
            context['data'] = data
            context['is_usecase'] = True
            return context
        raise Http404()


class ProductRetrieveAPIView(RetrieveAPIView):
    """商品情報取得API
    slugで指定
    """

    permission_classes = (AllowAny,)
    lookup_field = 'slug'
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        data = serializer.data
        if instance.category.get_parent_or_self().slug == 'cardboard':
            data['cardboard_colors'] = cardboard_colors
        return Response(data, status=status.HTTP_200_OK)


class ProductEstimationAPIView(APIView):
    """商品見積もりAPI
    単価/小計/版代/木型代/凹凸加工の型代/送料を税抜きで計算
    """
    permission_classes = (AllowAny,)

    def post(self, request, format=None, *args, **kwargs):
        slug = kwargs.get('slug')
        product = get_object_or_404(Product, slug=slug)
        options = request.data
        reordered = options.get('reordered', False)
        from_mydesign = options.get('from_mydesign', False)
        # TODO: VALIDATION
        #       - original size
        try:
            (unit_price, plate_price, mold_price, product_total, shipping_price, total_without_tax) = \
                product.get_prices(options, reordered, from_mydesign)
            tax = ceil(total_without_tax * settings.TAX_RATE)
            return Response({
                'unit_price': unit_price,
                'plate_price': plate_price,
                'mold_price': mold_price,
                'product_total': product_total,
                'shipping_price': shipping_price,
                'subtotal': total_without_tax,
                'tax': tax,
                'total': total_without_tax + tax,
            }, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({
                'message': "Invalid parameters",
                'required_fields': [_ for _ in product.extra_info['required_fields'].keys()]
            }, status=status.HTTP_400_BAD_REQUEST)


class ProductListEtimationAPIView(APIView):
    """商品見積もりAPI(リスト)
    単価/小計/版代/木型代/凹凸加工の型代/送料を税抜きで計算
    """
    permission_classes = (AllowAny,)

    def post(self, request, format=None, *args, **kwargs):
        slug = kwargs.get('slug')
        product = get_object_or_404(Product, slug=slug)

        data = request.data
        options = data.get('options')
        reordered = options.get('reordered', False)
        from_mydesign = options.get('from_mydesign', False)
        lots = data.get('lots')
        prices = {}
        # TODO: VALIDATION
        try:
            for lot in lots:
                options['quantity'] = lot
                (unit_price, plate_price, mold_price, product_total, shipping_price, total_without_tax) = \
                    product.get_prices(options, reordered, from_mydesign)
                tax = ceil(total_without_tax * settings.TAX_RATE)
                prices[lot] = {
                    'unit_price': unit_price,
                    'plate_price': plate_price,
                    'mold_price': mold_price,
                    'product_total': product_total,
                    'shipping_price': shipping_price,
                    'subtotal': total_without_tax,
                    'tax': tax,
                    'total': total_without_tax + tax,
                }
            return Response({
                'prices': prices
            }, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({
                'message': "Invalid parameters",
                'required_fields': [_.slug for _ in product.options.all()]
            }, status=status.HTTP_400_BAD_REQUEST)


class CategoryListAPIView(ListAPIView):

    permission_classes = (AllowAny,)

    serializer_class = ProductCategoryWithChildrenSerializer

    def get_queryset(self):
        root = ProductCategory.objects.filter(slug='root').first()
        if root:
            return ProductCategory.objects.public().filter(parent_category=root)
        return None


class CategoryRetrieveAPIView(APIView):

    permission_classes = (AllowAny,)

    def get(self, request, format=None, *args, **kwargs):
        slug = kwargs.get('slug')
        category = ProductCategory.objects.public().filter(slug=slug).first()
        if not category:
            return Response({}, status=status.HTTP_400_BAD_REQUEST)
        data = {}
        if category.has_children:
            data['categories'] = []
            for child in category.get_children():
                if "small-lot" not in child.slug:
                    data['categories'].append(self.get_category_data(child))
        else:
            category_data = self.get_category_data(category)
            data['categories'] = [category_data,]
        data['header'] = category.get_parent_or_self().extra_info
        return Response(data, status=status.HTTP_200_OK)

    def get_category_data(self, category):
        category_data = {
            'name': category.name,
            'slug': category.slug,
            'detail': category.detail,
            'tags': [{'name': tag.name,
                    #   'icon': tag.extra_info.get('icon', ""),
                      'url': tag.url} for tag in category.tags.all()]
        }
        products = Product.objects.filter(category=category, is_active=True)
        products_data = []

        for p in products:

            if 'small-lot' not in p.slug or p.slug == 'atype-fullcolor-small-lot':
                price = {
                    'unit': p.unit,
                    'value': p.price.sample_unit_price,
                    'lot': p.price.sample_lot,
                    'suffix': '円',
                }
                lots = {}
                small_lot = Product.objects.filter(slug=p.slug + '-small-lot', is_active=True).first()
                unit = p.unit if p.unit else '個'
                if small_lot:
                    lots[str(small_lot.info.min_ordering_quantity) + unit + " ~"] = small_lot.get_absolute_url()
                lots[str(p.info.min_ordering_quantity) + unit + " ~"] = p.get_absolute_url()

                products_data.append(
                    {'name': p.name,
                     'slug': p.slug,
                     'tags': [{'name': tag.name,} for tag in p.tags.all()],
                     'images': p.get_image_url_list(),
                     'example_images': p.get_example_image_url_list(),
                     'example_urls': p.get_example_url_list(),
                     'hover_image': p.get_hover_image_url(),
                     'url': p.get_absolute_url(),
                     'price': price,
                     'lots': lots}
                )
        category_data['products'] = products_data
        return category_data
