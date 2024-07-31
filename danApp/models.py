from django.db import models

# Create your models here.

class DanApp(models.Model):
  origin_country = models.CharField(max_length=64)
  destination_country = models.CharField(max_length=64)
  nights = models.models.models.IntegerField()
  price = models.models.models.IntegerField()
  
cd 