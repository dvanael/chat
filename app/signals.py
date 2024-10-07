from django.dispatch import receiver
from django.db.models.signals import post_save, pre_save
from django.contrib.auth.models import User
from .models import Profile, EmailAddress


@receiver(post_save, sender=User)
def user_postsave(sender, instance, created, **kwargs):
    user = instance

    if created:
        Profile.objects.create(
            user=user,
        )
    else:
        try:
            email_address = EmailAddress.objects.get(user=user)
            if email_address.email != user.email:
                email_address.email = user.email
                email_address.verified = False
                email_address.save()
        except:
            EmailAddress.objects.create(user=user, email=user.email, verified=False)


@receiver(pre_save, sender=User)
def user_presave(sender, instance, **kwargs):
    if instance.username:
        instance.username = instance.username.lower()
