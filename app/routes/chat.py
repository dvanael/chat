from django.urls import path
from app.views.chat import chat

urlpatterns = [
    path("", chat, name="chat"),
]
