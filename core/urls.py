from django.contrib import admin
from django.urls import path, include
from core.settings import DEBUG

urlpatterns = [
    path('', include('app.urls')),
]

if DEBUG:
    urlpatterns += [path('admin/', admin.site.urls)]