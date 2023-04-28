from django.db import models
from django.utils import timezone

# Create your models here.

class predict(models.Model):
    crime_commited = models.CharField(max_length=64)
    date = models.DateField(default="")
    time_hour = models.IntegerField(default=0)
    time_minute = models.IntegerField(default=0)
    country = models.CharField(max_length=64)
    state = models.CharField(max_length=64)
    district = models.CharField(max_length=64)
    city = models.CharField(max_length=64)
    block = models.CharField(max_length=64)
