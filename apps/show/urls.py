from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^index/$', views.index),
    url(r'^article/$', views.article),
    url(r'^test/$', views.test),
    url(r'^test_json/$', views.test_json),
    url(r'^test_add/$', views.test_add),
    url(r'^test_response/$', views.test_response),
    url(r'^upload_file/$', views.upload_file),
]