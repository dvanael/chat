from django.db import models
from django.contrib.auth.models import User


class ChatGroup(models.Model):
    group_name = models.CharField(max_length=100, unique=True, verbose_name="Nome do Grupo")
    users_online = models.ManyToManyField(User, related_name="users_online", blank=True, verbose_name="Usuários Online")

    def __str__(self):
        return self.group_name


class ChatGroupMessage(models.Model):
    group = models.ForeignKey(
        ChatGroup, related_name="messages", on_delete=models.CASCADE, verbose_name="Grupo"
    )
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Autor")
    body = models.CharField(max_length=300, verbose_name="Mensagem")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Data de Criação")

    def __str__(self):
        return f"{self.author.username} : {self.body}"

    class Meta:
        ordering = ["-created"]

