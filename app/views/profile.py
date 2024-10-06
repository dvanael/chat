from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.contrib.auth.views import redirect_to_login
from django.contrib import messages
from app.forms import ProfileForm


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
