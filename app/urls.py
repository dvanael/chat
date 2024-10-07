from django.urls import path, include
from app.routes import main, profile, email

urlpatterns = [
    path("", include(main)),
    path("perfil/", include(profile)),
    path("email/", include(email)),
]
