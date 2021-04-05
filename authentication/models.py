from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500)
    location = models.CharField(max_length=500)
    birthday = models.DateField(default=False)
    manage = models.BooleanField(default=False)


# @receiver(post_save, sender=User)
# def update(sender, created, instance, **kwargs):
#     if created:
#         Profile.objects.create(user=instance)
#         instance.profile.save()
