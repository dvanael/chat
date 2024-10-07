from django.urls import path
from app.views.profile import (
    profile_detail,
    profile_edit,
    profile_settings,
    profile_email_change,
    check_email,
)

urlpatterns = [
    path("", profile_detail, name="profile"),
    path("editar/", profile_edit, name="profile_edit"),
    path("onboarding/", profile_edit, name="profile_onboarding"),
    path("@<username>/", profile_detail, name="profile_detail"),
    path("configurar/", profile_settings, name="profile_settings"),
    path("email/atualizar/", profile_email_change, name="profile_email_change"),
    path("email/check/", check_email, name="profile_email_check"),
]
