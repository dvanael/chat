from django.contrib import admin
from .models import Profile, EmailAddress, ChatGroup, ChatGroupMessage

# Register your models here.
admin.site.register(Profile)
admin.site.register(EmailAddress)
admin.site.register(ChatGroup)
admin.site.register(ChatGroupMessage)
