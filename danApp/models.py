from django.db import models

# Create your models here.

class DanApp(models.Model):
  origin_country = models.CharField(max_length=64)
  destination_country = models.CharField(max_length=64)
  nights = models.IntegerField()
  price = models.IntegerField()
  
  # string rep. of tours
  def __str__(self):
    return(f"ID:{self.id}: From {self.origin_country} to {self.destination_country}, {self.nights} nights costs ${self.price}")
  