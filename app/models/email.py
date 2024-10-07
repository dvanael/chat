from django.db import models
from django.contrib.auth.models import User
from django.utils.crypto import get_random_string
from django.core.mail import EmailMultiAlternatives
from django.urls import reverse
from django.conf import settings
from django.template.loader import render_to_string
from django.utils.html import strip_tags

class EmailAddress(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField(unique=True)
    verified = models.BooleanField(default=False)
    verification_token = models.CharField(max_length=64, blank=True, null=True)

    def generate_verification_token(self):
        self.verification_token = get_random_string(64)
        self.save()

    def send_verification_email(self, request):
        protocol = "https" if request.is_secure() else "http"
        current_site = request.get_host()
        verification_link = f"{protocol}://{current_site}{reverse("email_verify", args=[self.verification_token])}"

        # vefication link in the terminal
        if settings.DEBUG:
            print(f"\nVerification link for debbuging.\n\n{verification_link}\n",)

        subject = "Verificação de Email"
        context = {}
        context["user"] = self.user
        context["verification_link"] = verification_link
        template_name = "email/verify_email.html"
        html_message = render_to_string(template_name, context)
        plain_message = strip_tags(html_message)

        message = EmailMultiAlternatives(
            subject = subject,
            body = plain_message,
            from_email = settings.DEFAULT_FROM_EMAIL,
            to = [self.email],
        )

        message.attach_alternative(html_message, "text/html")
        message.send()

    def __str__(self):
        return f"{self.user.username} - {self.email} - Verified: {self.verified}"
