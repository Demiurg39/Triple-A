from django.contrib.auth import views as auth_views
from django.urls import path

from . import views

app_name = "account"

urlpatterns = [
    # URL for login
    path("login/", auth_views.LoginView.as_view(), name="login"),
    # URL for logout
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    # URL for registration
    path("edit/", views.edit, name="edit"),
    path("register/", views.register, name="register"),
    # URL to reset, change password
    # password change
    path(
        "password-change/",
        auth_views.PasswordChangeView.as_view(),
        name="password_change",
    ),
    path(
        "password-change-done/",
        auth_views.PasswordChangeDoneView.as_view(),
        name="password_change_done",
    ),
    # password reset
    path(
        "password-reset/",
        auth_views.PasswordResetView.as_view(),
        name="password_reset",
    ),
    path(
        "password-reset-done/",
        auth_views.PasswordResetDoneView.as_view(),
        name="password_reset_done",
    ),
    path(
        "password-reset/<uidb64>/<token>/",
        auth_views.PasswordResetConfirmView.as_view(),
        name="password_reset_confirm",
    ),
    path(
        "password_reset/complete/",
        auth_views.PasswordResetCompleteView.as_view(),
        name="password_reset_complete",
    ),
]
