from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import ListAPIView, RetrieveAPIView
from .models import MyDesign
from .serializers import MyDesignSerializer, MyDesignReorderSerializer
import json


@method_decorator(login_required, name='dispatch')
class MyDesignListAPIView(ListAPIView):
    """ Mydesign一覧
    """

    serializer_class = MyDesignSerializer

    def get_queryset(self):
        return MyDesign.objects.filter(user=self.request.user)


@method_decorator(login_required, name='dispatch')
class MyDesignRenameAPIView(APIView):
    """ Mydesign名前変更
    """

    def post(self, request, format=None, **kwargs):
        md_id = kwargs.get('id', None)
        md = MyDesign.objects.filter(id=md_id).first()
        if md:
            new_name = request.data.get('name')
            md.name = new_name
            md.save()
            return Response({'message': "Successfully uploaded."}, status=status.HTTP_200_OK)
        return Response({'message': "Something went wrong."}, status=status.HTTP_400_BAD_REQUEST)


class MyDesignReorderRetrieveAPIView(RetrieveAPIView):
    serializer_class = MyDesignReorderSerializer
    lookup_field = 'id'

    def get_queryset(self):
        user = self.request.user
        return MyDesign.objects.filter(user=user)
