from . import views
from django.urls import path

urlpatterns = [
    path("signup/", views.UserRegistrationView.as_view(), name="user_registration"),
    path("signin/", views.login_view, name="user_signin"),
    path("logout/", views.UserLogoutView.as_view(), name="user_logout"),
]
