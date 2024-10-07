from django.shortcuts import get_object_or_404, redirect
from django.http import HttpResponse
from app.models import EmailAddress
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django.contrib import messages


def send_verification_email(request):

    if request.htmx:
        email_address = get_object_or_404(EmailAddress, user=request.user)
        if not email_address.verified:
            email_address.generate_verification_token()
            email_address.send_verification_email(request)
            return HttpResponse("Enviado. Verifique seu email.")
    else:
        return redirect("profile_settings")


def verify_email(request, token):
    email_address = get_object_or_404(EmailAddress, verification_token=token)
    if email_address.verified:
        messages.warning(request, "Email ja foi verificado")
    else:
        messages.success(request, "Email verificado com sucesso!")

    email_address.verified = True
    email_address.verification_token = None
    email_address.save()

    return redirect("profile_settings")


def check_email(request):

    if request.htmx:
        email = request.GET.get("email")

        try:
            validate_email(email)
            email_exists = (
                User.objects.filter(email=email).exclude(id=request.user.id).exists()
            )
            if email_exists:
                return HttpResponse(f"Esse email já está em uso.")
            else:
                return HttpResponse(f"Email poggers!")
        except ValidationError:
            return HttpResponse(f"Digite um email válido.")

    else:
        return redirect("profile_settings")
