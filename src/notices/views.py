import json
from datetime import datetime
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_protect
from rest_framework import status, pagination
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import RetrieveAPIView, ListAPIView
from rest_framework.permissions import AllowAny
from .models import Notice, NoticePost
from .serializers import NoticePostSerializer, NoticeListSerializer

import logging
logger = logging.getLogger(__name__)

class StandardResultsSetPagination(pagination.PageNumberPagination):
    page_size = 10

    def get_paginated_response(self, data):
        return Response({
            'count': self.page.paginator.count,
            'next': self.get_next_link(),
            'previous': self.get_previous_link(),
            'current_page': self.page.number,
            'results': data
        })

@method_decorator(login_required, name='dispatch')
class NoticeListView(ListView):

    template_name = "notices/notice_list.html"
    model = Notice
    paginate_by = 15

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        return context

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(users=self.request.user).order_by('created_at').reverse()

class NoticePostDetailView(DetailView):

    template_name = "notices/notice_detail.html"
    model = NoticePost


class NoticePostDetailAPIView(RetrieveAPIView):

    serializer_class = NoticePostSerializer 

    def get_queryset(self):
        user = self.request.user
        return NoticePost.objects.filter(users=user,)

class NoticeReadAPIView(APIView):

    permission_classes = (AllowAny,)

    def post(self, request, format=None):
        try:
            data = request.data
            user = request.user
            notice = Notice.objects.get(id=data.get("notice_id"))
            notice.noticeread_set.filter(users_id=user.id).update(read_at=datetime.now())
            if hasattr(notice, 'noticereminder'):
                return Response(reverse('order_history_item', kwargs={'ref_code':notice.noticereminder.orderitem.ref_code}))
            elif hasattr(notice, 'noticepost'):
                return Response(reverse('notice_post',args=[notice.id]))
            else:
                return Response({'message': "Something went wrong."}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            logger.info(e)
            return Response({'message': "Something went wrong."}, status=status.HTTP_400_BAD_REQUEST)

class NoticeListAPIView(ListAPIView):

    serializer_class = NoticeListSerializer
    pagination_class = StandardResultsSetPagination

    def get_queryset(self):
        return Notice.objects.filter(users=self.request.user).order_by('created_at').reverse()