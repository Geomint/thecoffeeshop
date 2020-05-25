from django.conf.urls import url
from .views import cart_contents_view

urlpatterns = [
    url(r'^$', cart_contents_view, name='cart'),
]