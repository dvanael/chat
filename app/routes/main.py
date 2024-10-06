from django.urls import path
from django.contrib.auth.views import LoginView
from app.views.main import index, logout_view, register

urlpatterns = [
    path("", index, name="index"),
    path("logout/", logout_view, name="logout"),
    path("login/", LoginView.as_view(), name="login"),
    path("cadastro/", register, name="register"),
]
