from django.contrib.auth import views as auth_views
from django.urls import include, path

from . import views

urlpatterns = [
    # URL for login
    path("login/", auth_views.LoginView.as_view, name="login"),
    # URL for logout
    path("logout/", auth_views.LogoutView.as_view, name="logout"),
    # URL for registration
    path("register/", views.register, name="register"),
    # URL to reset, change password
    path("", include("django.contrib.auth.urls")),
]
