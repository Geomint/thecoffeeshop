from django.conf.urls import url, include
from .views import view_all_products

urlpatterns = [
    url(r'^$', view_all_products, name='View All Products')
]