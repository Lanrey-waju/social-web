from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser

# Create your models here.
CustomUser = get_user_model()


class CustomUserManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_active=True)


class CustomUser(AbstractUser):
    objects = CustomUserManager()
