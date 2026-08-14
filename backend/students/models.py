from django.db import models
from accounts.models import Tutor
# Create your models here.

class Student(models.Model):
    tutor = models.ForeignKey(Tutor, on_delete=models.CASCADE, related_name='st_tutor')
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    school_name = models.CharField(max_length=255)


    def __str__(self):
        return self.name