from django.db import models
from django.contrib.auth.models import User
from django.utils.crypto import get_random_string
from django.core.mail import send_mail
from django.urls import reverse
from django.conf import settings


class EmailAddress(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField(unique=True)
    verified = models.BooleanField(default=False)
    verification_token = models.CharField(max_length=64, blank=True, null=True)

    def generate_verification_token(self):
        self.verification_token = get_random_string(64)
        self.save()

    def send_verification_email(self):
        verification_link = settings.SITE_URL + reverse(
            "verify_email", args=[self.verification_token]
        )
        subject = "Please verify your email address"
        message = f"Hi {self.user.username},\n\nPlease verify your email by clicking the link below:\n\n{verification_link}"
        send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [self.email])

    def __str__(self):
        return f"{self.user.username} - {self.email} - Verified: {self.verified}"
