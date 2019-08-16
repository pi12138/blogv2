from rest_framework import serializers
from .models import UploadFileInfo


class UploadFileInfoSerializer(serializers.ModelSerializer):
    url = serializers.SerializerMethodField(method_name="get_url")

    class Meta:
        model = UploadFileInfo
        exclude = ('file_url', )
        extra_kwargs = {
            'size': {'read_only': True}, 
            'filename': {'read_only': True}, 
            'upload_time': {'format': "%Y-%m-%d %H:%M:%S", 'read_only': True}
        }

    def get_url(self, obj):
        return "http://pwazr0238.bkt.clouddn.com/{}".format(obj.file_url)