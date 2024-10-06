from django.urls import path, include
from app.routes import main

urlpatterns = [
    path('', include(main)),
]


