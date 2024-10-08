import json
from channels.generic.websocket import WebsocketConsumer
from django.shortcuts import get_object_or_404
from django.template.loader import render_to_string
from app.models import ChatGroup, ChatGroupMessage
from asgiref.sync import async_to_sync


class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.user = self.scope["user"]
        self.chat_group_name = self.scope["url_route"]["kwargs"]["chat_group"]
        self.chat_group = get_object_or_404(ChatGroup, group_name=self.chat_group_name)

        async_to_sync(self.channel_layer.group_add)(
            self.chat_group_name,
            self.channel_name,
        )
        if self.user not in self.chat_group.users_online.all():
            self.chat_group.users_online.add(self.user)
            self.update_online_count()

        self.accept()

    def disconnect(self, close_code):
        if self.user in self.chat_group.users_online.all():
            self.chat_group.users_online.remove(self.user)
            self.update_online_count()

        async_to_sync(self.channel_layer.group_discard)(
            self.chat_group_name,
            self.channel_name,
        )

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        body = text_data_json["body"]

        message = ChatGroupMessage.objects.create(
            body=body,
            author=self.user,
            group=self.chat_group,
        )

        event = {}
        event["type"] = "message_handler"
        event["message_id"] = message.id

        async_to_sync(self.channel_layer.group_send)(
            self.chat_group_name,
            event,
        )

    def message_handler(self, event):
        partial_template = "partials/chat/message.html"
        context = {}

        message_id = event["message_id"]
        message = get_object_or_404(ChatGroupMessage, id=message_id)

        context["message"] = message
        context["user"] = self.user

        html = render_to_string(
            template_name=partial_template,
            context=context,
        )
        self.send(text_data=html)

    def update_online_count(self):
        online_count = self.chat_group.users_online.count() - 1

        event = {}
        event["type"] = "online_count_handler"
        event["online_count"] = online_count

        async_to_sync(self.channel_layer.group_send)(
            self.chat_group_name,
            event,
        )

    def online_count_handler(self, event):
        partial_template = "partials/chat/online_count.html"
        context = {}

        online_count = event["online_count"]
        context["online_count"] = online_count
        html = render_to_string(
            template_name=partial_template,
            context=context,
        )
        self.send(text_data=html)
