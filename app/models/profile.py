from django.db import models
from django.contrib.auth.models import User
from django.conf import settings


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name="Usuário")
    displayname = models.CharField(max_length=30, null=True, blank=True, verbose_name="Nome de Exibição")
    picture = models.ImageField(upload_to="profile_pics/", null=True, blank=True, verbose_name="Foto de Perfil")
    bio = models.TextField(null=True, blank=True, verbose_name="Biografia")

    def __str__(self):
        return str(self.user)

    @property
    def name(self):
        if self.displayname:
            return self.displayname
        return self.user.username

    @property
    def avatar(self):
        if self.picture:
            return self.picture.url
        return f"{settings.STATIC_URL}img/default_pfp.png"

