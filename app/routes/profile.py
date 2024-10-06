from django.urls import path
from app.views.profile import (
    profile_detail,
    profile_edit,
)

urlpatterns = [
    path("", profile_detail, name="profile_detail"),
    path("editar/", profile_edit, name="profile_edit"),
    path("onboarding/", profile_edit, name="profile_onboarding"),
]
