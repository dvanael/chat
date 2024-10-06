from django.shortcuts import render, redirect
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.decorators import login_required
from app.forms import UserForm


def index(request):
    template_name = "index.html"
    context = {}
    context["key"] = "hello world"
    return render(request, template_name, context)


@login_required
def logout_view(request):
    logout(request)
    return redirect("index")


def register(request):
    template_name = "registration/register.html"
    context = {}

    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password1"]
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("profile_onboarding")

    if request.method == "GET":
        form = UserForm()

    context["form"] = form
    return render(request, template_name, context)
