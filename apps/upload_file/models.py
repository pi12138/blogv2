from django.db import models

# Create your models here.


class UploadFileInfo(models.Model):
    filename = models.CharField(max_length=100, verbose_name="文件名")
    file_url = models.CharField(max_length=300, verbose_name="文件url")
    size = models.IntegerField(verbose_name="文件大小", null=True, blank=True)
    upload_time = models.DateTimeField(auto_now_add=True, verbose_name="上传时间", null=True, blank=True)

    def qiniu_file_url(self):
        return "http://pwazr0238.bkt.clouddn.com/{}".format(self.file_url)