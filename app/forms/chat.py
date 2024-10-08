from django.forms import ModelForm
from django.urls import reverse_lazy
from django import forms
from django.contrib.auth.models import User
from app.models import ChatGroupMessage


class ChatMessageForm(forms.ModelForm):
    class Meta:
        model = ChatGroupMessage
        fields = ["body"]
        widgets = {
            "body": forms.TextInput(
                attrs={"placeholder": "Message", "autofocus": True}
            ),
        }
