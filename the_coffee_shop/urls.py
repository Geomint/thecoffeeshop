"""the_coffee_shop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from pages.views import index, about_view, contact_us_view
from products import urls as urls_products
from accounts import urls as urls_accounts
from cart import urls as urls_cart
from search import urls as urls_search
from pages import urls as urls_pages
from checkout import urls as urls_checkout

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', index, name="home"),
    url(r'about$', about_view, name="about"),
    url(r'contact$', contact_us_view, name="contact"),
    url(r'products/', include(urls_products)),
    url(r'', include(urls_pages)),
    url(r'accounts/', include(urls_accounts)),
    url(r'search/', include(urls_search)),
    url(r'cart/', include(urls_cart)),
    url(r'checkout/', include(urls_checkout)),
]
