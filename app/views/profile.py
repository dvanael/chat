from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.views import redirect_to_login
from django.contrib import messages
from app.forms import ProfileForm, EmailForm


def profile_detail(request, username=None):
    template_name = "profile/page.html"
    context = {}

    if username:
        profile = get_object_or_404(User, username=username).profile
    else:
        try:
            profile = request.user.profile
        except:
            return redirect_to_login(request.get_full_path())

    context["profile"] = profile
    return render(request, template_name, context)


@login_required
def profile_edit(request):
    template_name = "profile/edit.html"
    context = {}
    form = ProfileForm(instance=request.user.profile)

    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            form.save()
            return redirect("profile_detail")

    if request.path == reverse("profile_onboarding"):
        onboarding = True
    else:
        onboarding = False

    context["form"] = form
    context["onboarding"] = onboarding
    return render(request, template_name, context)


@login_required
def profile_settings(request):
    template_name = "profile/settings.html"
    return render(request, template_name)


@login_required
def profile_email_change(request):
    template_name = "partials/email_form.html"
    context = {}

    if request.htmx:
        form = EmailForm(instance=request.user)
        context["form"] = form
        return render(request, template_name, context)

    if request.method == "POST":
        form = EmailForm(request.POST, instance=request.user)

        if form.is_valid():

            # Check if the email already exists
            email = form.cleaned_data["email"]
            if User.objects.filter(email=email).exclude(id=request.user.id).exists():
                messages.warning(request, f"{email} is already in use.")
                return redirect("profile_settings")

            form.save()

            # Then Signal updates emailaddress and set verified to False

            # Then send confirmation email
            messages.success(request, "Saved")
            return redirect("profile_settings")
        else:
            messages.warning(request, "Form not valid")
            return redirect("profile_settings")
    return redirect("index")
