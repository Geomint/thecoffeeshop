from django.conf.urls import url, include
from .views import view_all_products, view_product_detail

urlpatterns = [
    url(r'^$', view_all_products, name='View All Products'),
    url(r'(?P<id>\d+)', view_product_detail, name='view_product_detail')
]