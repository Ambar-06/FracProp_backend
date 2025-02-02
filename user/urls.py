from . import views
from django.urls import path


urlpatterns = [
    path("auth/signup", views.UserSignUp.as_view(), name="signup"),
    path("auth/login", views.UserLogin.as_view(), name="login"),
    path("profile", views.UserProfileView.as_view(), name="profile"),
    path("send-email-otp", views.SendEmailOTP.as_view(), name="send-email-otp"),
    path("verify-email", views.VerifyEmail.as_view(), name="verify-email"),
    path("reset-password", views.ResetPassword.as_view(), name="reset-password"),
    path("change-password", views.ChangePassword.as_view(), name="change-password"),
    path("dashboard", views.DashboardView.as_view(), name="dashboard"),
]
