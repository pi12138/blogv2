from django.conf.urls import url
from rest_framework.routers import DefaultRouter
from . import views


router = DefaultRouter()
router.register(r'files', views.Files, base_name='files')
urlpatterns = router.urls

urlpatterns += [
    url(r'qiniu_callback/$', views.qiniu_callback),
]
