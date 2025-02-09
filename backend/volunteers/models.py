from django.db import models

# Create your models here.
from django.db import models

class Volunteer(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, unique=True)
    skills = models.TextField()
    availability = models.CharField(max_length=100)

    def __str__(self):
        return self.full_name
