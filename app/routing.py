from django.urls import path
from .consumers import ChatConsumer

websocket_urlpatterns = [
    path("ws/chat_group/<chat_group>/", ChatConsumer.as_asgi()),
    # path("ws/online-status/", OnlineStatusConsumer.as_asgi()),
]
