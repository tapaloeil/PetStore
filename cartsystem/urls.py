from django.conf.urls import url
from . import views
from .views import api_add_to_cart,api_remove_from_cart,api_get_cart_count,api_sync_cart

urlpatterns = [
    url(r'^add/(?P<product_ref_id>(\d+))/(?P<quantity>(\d+))/$', views.add_to_cart, name='add_to_cart'),
    url(r'^api/add/$', api_add_to_cart.as_view(), name='api_add_to_cart'),
    url(r'^remove/(?P<product_ref_id>\d+)/$', views.remove_from_cart, name="remove_from_cart"),
    url(r'^api/remove/$', api_remove_from_cart.as_view(), name="api_remove_from_cart"),
    url(r'^checkout/$', views.get_chart, name="get_cart"),
    url(r'^api/count/$', api_get_cart_count.as_view(), name="api_get_cart_count"),
    url(r'^api/sync/$', api_sync_cart.as_view(), name="api_sync_cart"),
]
