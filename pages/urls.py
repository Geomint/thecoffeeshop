from django.conf.urls import url
from .views import contact_us_view

urlpatterns = [
    url(r'send/message/', contact_us_view, name='send')
]