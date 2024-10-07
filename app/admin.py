from django.contrib import admin
from .models import Profile, EmailAddress

# Register your models here.
admin.site.register(Profile)
admin.site.register(EmailAddress)
