from django.contrib.auth.models import AbstractUser
from accounts.models import CustomUser  
from django.db import models

class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=15, unique=True, null=True, blank=True)

    class Meta:
        app_label = 'accounts'  
