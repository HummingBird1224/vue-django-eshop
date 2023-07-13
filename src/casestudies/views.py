from django.shortcuts import render

from django.conf import settings
from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from django.shortcuts import get_object_or_404
from django.http import Http404
from django.db.models import Q
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.generics import RetrieveAPIView, ListAPIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

from .models import CaseStudy, CaseStudyCategory
from products.models import ProductCategory

from .serializers import CaseStudySerializer, CaseStudyCategoryWithChildrenSerializer, CaseStudyCategorySerializer
from products.serializers import ProductCategorySerializer

# Create your views here.
class CaseStudyList1View(TemplateView):
    """商品一覧
    カテゴリとユースケースがある
    """

    template_name = 'casestudies/casestudy_list.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['casestudies'] = CaseStudy.objects
        return context


class CaseStudyCategoryView(TemplateView):
    """商品一覧
    カテゴリとユースケースがある
    """

    template_name = 'casestudies/casestudy_list.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        category = kwargs.get('category')
        tag = kwargs.get('tag')
        category_root = get_object_or_404(CaseStudyCategory, slug='root')
        if category == 'all':
            context['casestudies'] = CaseStudy.objects.public().filter(product_category=category_root)
        else:
            context['casestudies'] = []

        # CATEGORY
        if tag != 'all':
            category = CaseStudyCategory.objects.filter(category=tag).first()
            if category:
                # EXCLUDE EXTERNALS
                if category.get_parent_or_self().slug == 'external':
                    raise Http404()
                context['category'] = category
                context['parent_category'] = category.get_parent_or_self()
                return context
        else:
            return context

        raise Http404()


class CaseStudyCategoryTagView(TemplateView):
    """商品一覧
    カテゴリとユースケースがある
    """

    template_name = 'casestudies/casestudy_list.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        category = kwargs.get('category')
        tag = kwargs.get('tag')
        category_root = get_object_or_404(CaseStudyCategory, slug='root')
        if category == 'all':
            context['casestudies'] = CaseStudy.objects.public().filter(product_category=category_root)
        else:
            context['casestudies'] = []

        # CATEGORY
        # if  category == 'product_category':
        #     category = ProductCategory.objects.filter(slug=tag).first()
        #     if category:
        #         # EXCLUDE EXTERNALS
        #         if category.get_parent_or_self().slug == 'external':
        #             raise Http404()
        #         context['category'] = category
        #         context['parent_category'] = category.get_parent_or_self()
        #         return context
        if tag != 'all':
            category = CaseStudyCategory.objects.filter(slug=tag).first()
            if category:
                # EXCLUDE EXTERNALS
                if category.get_parent_or_self().slug == 'external':
                    raise Http404()
                context['category'] = category
                context['parent_category'] = category.get_parent_or_self()
                return context
        else:
            return context

        raise Http404()


class CaseStudyDetailView(DetailView):
    """商品詳細ページ
    カテゴリごとにテンプレートの切り替え
    """
    related_products_num = 3
    template_name = 'casestudies/casestudy_detail.html'
    def get_object(self, *args, **kwargs):
        global slug
        slug = self.kwargs.get('slug', None)
        obj = get_object_or_404(CaseStudy, slug=slug)
        # EXCLUDE EXTERNAL PRODUCTS
        # if obj.category.get_parent_or_self().slug == 'external':
        #     raise Http404()
        # obj.parent_category = obj.category.get_parent_or_self()
        return obj

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['static_url'] = settings.STATIC_URL
        context['category'] = self.kwargs.get('category', None)
        context['tag'] = self.kwargs.get('tag', None)
        context['slug'] = slug
        # 関連商品同じジャンルの中からランダムで三つ
        # context['related_products'] = self.get_related_products()
        context['object']=self.get_object()
        return context

    # def get_related_products(self):
    #     products = CaseStudy.objects.filter(category=self.object.category).exclude(slug=self.object.slug)
    #     return products.order_by('?')[:self.related_products_num]


class CaseStudyRetrieveAPIView(RetrieveAPIView):
    """商品情報取得API
    slugで指定
    """

    permission_classes = (AllowAny,)
    lookup_field = 'slug'
    queryset = CaseStudy.objects.all()
    serializer_class = CaseStudySerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)       
        data = serializer.data
        return Response(data, status=status.HTTP_200_OK)


class CaseStudyListAPIView(ListAPIView):

    
    permission_classes = (AllowAny,)

    def get(self, request, format=None, *args, **kwargs):
        category=kwargs.get('category')
        tag=kwargs.get('tag')
        if category == 'all':
            queryset=CaseStudy.objects.public()
            category_serializer = None
        else :
            # if category == 'product_category' :
            #     parent_category = get_object_or_404(ProductCategory, is_active=True, slug=tag)
            #     children_category_instance=ProductCategory.objects.public().filter(is_active=True, parent_category_id=parent_category.id)
            #     category_serializer = ProductCategorySerializer(parent_category) 
            # else :
            parent_category = get_object_or_404(CaseStudyCategory, is_active=True, slug=tag)
            children_category_instance=parent_category.get_children()
            category_serializer = CaseStudyCategorySerializer(parent_category) 

            if not children_category_instance :
                query = Q(**{f"{category}": parent_category.id})
            else :
                query=Q(**{f"{category}": parent_category.id })
                for children_category in children_category_instance:
                    query=query | Q(**{f"{category}": children_category.id })
                # query = Q(**{f"{category}": parent_category.id }) | Q(**{f"{category}": children_category.id })
            queryset=CaseStudy.objects.public().filter(query)
            # casestudy_category=CaseStudyCategory.objects.public().filter(slug=tag)
            # category_serializer=CaseStudyCategorySerializer(casestudy_category, many=True)

        serializer=CaseStudySerializer(queryset, many=True)
        return Response({"casestudy_list":serializer.data, "category_object":category_serializer.data if category_serializer else None})

class CaseStudySameTagListAPIView(ListAPIView):

    
    permission_classes = (AllowAny,)

    def get(self, request, format=None, *args, **kwargs):
        category=kwargs.get('category')
        tag=kwargs.get('tag')
        slug=kwargs.get('slug')
        if category == 'all':
            queryset=CaseStudy.objects.public()
        else :
            # if category == 'product_category' :
            #     parent_category = get_object_or_404(ProductCategory, is_active=True, slug=tag)
            #     children_category_instance=ProductCategory.objects.public().filter(is_active=True, parent_category_id=parent_category.id)
            # else :
            parent_category = get_object_or_404(CaseStudyCategory, is_active=True, slug=tag)
            children_category_instance=parent_category.get_children()

            if not children_category_instance :
                query = Q(**{f"{category}": parent_category.id})
            else :
                query=Q(**{f"{category}": parent_category.id })
                for children_category in children_category_instance:
                    query=query | Q(**{f"{category}": children_category.id })
                # query = Q(**{f"{category}": parent_category.id }) | Q(**{f"{category}": children_category.id })

            queryset=CaseStudy.objects.public().filter(query).exclude(slug=slug)

        serializer=CaseStudySerializer(queryset, many=True)
        return Response(serializer.data)

     

class CaseStudyCategoryListAPIView(ListAPIView):

    permission_classes = (AllowAny,)

    serializer_class = CaseStudyCategoryWithChildrenSerializer

    def get_queryset(self):
        root = CaseStudyCategory.objects.filter(slug='root').first()
        if root:
            return CaseStudyCategory.objects.public().filter(category=root)
        return None



class CaseStudyCategoryRetrieveAPIView(APIView):

    permission_classes = (AllowAny,)

    def get(self, request, format=None, *args, **kwargs):
        slug = kwargs.get('slug')
        category = CaseStudyCategory.objects.public().filter(slug=slug).first()
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
                      'icon': tag.extra_info.get('icon', ""),
                      'url': tag.url} for tag in category.tags.all()]
        }
        case_studies = CaseStudy.objects.filter(category=category, is_active=True)
        case_studies_data = []

        for p in case_studies:

            if 'small-lot' not in p.slug or p.slug == 'atype-fullcolor-small-lot':
                price = {
                    'unit': p.unit,
                    'value': p.price.sample_unit_price,
                    'lot': p.price.sample_lot,
                    'suffix': '円',
                }
                lots = {}
                small_lot = CaseStudy.objects.filter(slug=p.slug + '-small-lot', is_active=True).first()
                unit = p.unit if p.unit else '個'
                if small_lot:
                    lots[str(small_lot.info.min_ordering_quantity) + unit + " ~"] = small_lot.get_absolute_url()
                lots[str(p.info.min_ordering_quantity) + unit + " ~"] = p.get_absolute_url()

                case_studies.append(
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
        category_data['case_studies'] = case_studies_data
        return category_data
