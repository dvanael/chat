from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from app.models import ChatGroup
from app.forms import ChatMessageForm


@login_required
def chat(request):
    template_name = "chat/page.html"
    context = {}
    chat_group = get_object_or_404(ChatGroup, group_name="Global")
    chat_messages = chat_group.messages.all()[:30]
    form = ChatMessageForm()

    if request.htmx:
        partial_template = "partials/chat/message.html"
        form = ChatMessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.author = request.user
            message.group = chat_group
            form.save()
            context["message"] = message
            context["user"] = request.user
            return render(request, partial_template, context)

    context["chat_group"] = chat_group
    context["chat_messages"] = chat_messages
    context["form"] = form
    return render(request, template_name, context)
