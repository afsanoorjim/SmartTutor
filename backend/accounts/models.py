from django.db import models
from django.contrib.auth.models import AbstractUser

from .managers import CustomUserManager

class Tutor(AbstractUser):
    username = None  # Remove the username field
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=100)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']
    objects = CustomUserManager()
    def __str__(self):
        return self.name