from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Menu(models.Model):
    coffee = models.CharField(max_length=255, blank=False, unique=True)
    price = models.DecimalField(max_digits=15, decimal_places=3)
