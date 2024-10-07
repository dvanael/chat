from django.urls import path
from app.views.email import verify_email, check_email, send_verification_email

urlpatterns = [
    path("check/", check_email, name="email_check"),
    path("verificar/<str:token>/", verify_email, name="email_verify"),
    path("send_verification/", send_verification_email, name="email_verification"),
]
