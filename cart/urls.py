from django.conf.urls import url
from .views import cart_contents_view, add_to_cart_view

urlpatterns = [
    url(r'^view/', cart_contents_view, name='cart'),
    url(r'^add/(?P<id>\d+)', add_to_cart_view, name='addtocart')
]