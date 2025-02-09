from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class DisasterReport(models.Model):
    title = models.CharField(max_length=255, default="Unknown Title")  # Default value
    description = models.TextField(default="No description available")  # Default value
    location = models.CharField(max_length=255, default="Unknown Location")  # Default value
    created_at = models.DateTimeField(auto_now_add=True)


class Donation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    transaction_id = models.CharField(max_length=255, unique=True)
    status = models.CharField(max_length=20, default='Pending')
    created_at = models.DateTimeField(auto_now_add=True)