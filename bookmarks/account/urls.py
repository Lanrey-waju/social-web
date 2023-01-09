from django.urls import path
from django.contrib.auth import views as auth_views

from .views import HomePageView, SignUpPageView

urlpatterns = [
    #     path("login", auth_views.LoginView.as_view(), name="login"),
    #     path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    #     path(
    #         "password-reset/", auth_views.PasswordResetView.as_view(), name="password_reset"
    #     ),
    #     path(
    #         "password-reset/done",
    #         auth_views.PasswordResetDoneView.as_view(),
    #         name="password_reset_done",
    #     ),
    #     path(
    #         "password-change/",
    #         auth_views.PasswordChangeView.as_view(),
    #         name="password_change",
    #     ),
    #     path(
    #         "password-reset/done/",
    #         auth_views.PasswordResetDoneView.as_view(),
    #         name="password_creset_done",
    #     ),
    path("", HomePageView.as_view(), name="home"),
    path("signup/", SignUpPageView.as_view(), name="signup"),
]
