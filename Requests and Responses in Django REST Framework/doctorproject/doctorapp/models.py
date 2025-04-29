from django.db import models

# Create your models here.

class Doctor(models.Model):
    name = models.CharField(max_length=20)
    specialty = models.CharField(max_length=50)
    phone = models.CharField(max_length=10)
    email = models.EmailField()

    def __str__(self):
        return self.name