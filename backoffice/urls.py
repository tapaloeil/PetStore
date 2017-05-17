from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.p_list, name='p_list'),
    url(r'^product/(?P<pk>\d+)/$', views.p_detail, name='p_detail'),
]