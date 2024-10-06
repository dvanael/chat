from django.shortcuts import render


def index(request):
    template_name = 'index.html'
    context = {}
    context['key'] = 'hello world'
    return render(request, template_name, context)