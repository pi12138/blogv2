from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, action
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from .models import UploadFileInfo
from .serializers import UploadFileInfoSerializer
from .helper import QiniuOSS
# Create your views here.


@api_view(http_method_names=['GET','POST'])
def qiniu_callback(request):
    # print("callbackBody: {}".format(request.data))
    filename = request.data.get('filename', "")
    file_url = request.data.get('qiniu_key', "")
    size = request.data.get('filesize', 0)

    # print("filename: {}, file_url: {}".format(filename, file_url, size))
    if not all([filename, file_url, size]):
        return Response("文件信息不全")

    UploadFileInfo.objects.create(filename=filename, file_url=file_url, size=size)

    return Response(status=status.HTTP_200_OK)


class Files(viewsets.ModelViewSet):
    queryset = UploadFileInfo.objects.all()
    serializer_class = UploadFileInfoSerializer

