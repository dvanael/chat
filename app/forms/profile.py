from django.forms import ModelForm
from django.urls import reverse_lazy
from django import forms
from django.contrib.auth.models import User
from app.models import Profile


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ["picture", "displayname", "bio"]
        widgets = {
            "picture": forms.FileInput(),
            "displayname": forms.TextInput(),
            "bio": forms.Textarea(),
        }


class EmailForm(ModelForm):
    email = forms.EmailField(
        max_length=100,
        widget=forms.EmailInput(
            attrs={
                "placeholder": "Email",
                "hx-get": reverse_lazy("email_check"),
                "hx-trigger": "keyup changed delay:500ms",
                "hx-target": "#email-check",
            }
        ),
    )

    class Meta:
        model = User
        fields = ["email"]
