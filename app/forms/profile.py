from django.forms import ModelForm
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
