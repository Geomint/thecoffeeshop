from django.conf.urls import url
from .views import checkout_view

urlpatterns = [
    url(r'^$', checkout_view, name='checkout')
]