from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^add/(?P<product_ref_id>\d+)/(?P<quantity>\d+)/$', views.add_to_cart, name='add_to_cart'),
    url(r'^remove/(?P<product_ref_id>\d+)/$', views.remove_from_cart, name="remove_from_cart"),
    url(r'^checkout/$', views.get_chart, name="get_cart"),
    #url(r'', views.get_chart, name="get_chart"),
]