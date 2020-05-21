from django.contrib.auth import views as auth_views
from django.conf.urls import url
from .views import register_account_view, login_account_view, account_profile_view

urlpatterns = [
    url(r'register/', register_account_view, name="register"),
    url(r'login/', auth_views.LoginView.as_view(template_name='login.html', redirect_authenticated_user=True), name="login"),
    url(r'logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name="logout"),
    url(r'profile/', account_profile_view, name="profile"),
]