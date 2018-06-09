from django.db import models

# Create your models here.

class Phone(models.Model):
    brand = models.CharField(blank=True, max_length=100)
    operating_system = models.CharField(blank=True, max_length=100)
    data_transfer = models.CharField(blank=True, max_length=100)
    processor_speed = models.DecimalField(max_digits=2, decimal_places=1)
    price = models.IntegerField(blank=True, null=True)
