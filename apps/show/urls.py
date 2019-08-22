from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^hello/$', views.hello),
    url(r'^index/$', views.index),
    url(r'^article/(?P<pk>\d+)/$', views.article),
    url(r'^search/$', views.search),
    url(r'^archive/$', views.archive),
    url(r'^message_board/$', views.message_board),
    url(r'^user_statistics/$', views.user_statistics),

    
    url(r'^test/$', views.test),
    url(r'^test_json/$', views.test_json),
    url(r'^test_add/$', views.test_add),
    url(r'^test_response/$', views.test_response),
    url(r'^upload_file/$', views.upload_file),
]