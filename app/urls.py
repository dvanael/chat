from django.urls import path, include
from app.routes import main, profile

urlpatterns = [
    path("", include(main)),
    path("perfil/", include(profile)),
]
