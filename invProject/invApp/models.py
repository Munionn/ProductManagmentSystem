from django.db import models
from django.db.models.base import Model

# Cmereate your models here.

class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    price = models.FloatField()
    name = models.CharField(max_length=100)
    quantity = models.IntegerField()
    sku = models.CharField(max_length=50, unique=True)
    supplier = models.CharField(max_length=100)
    product_Type = models.CharField(max_length=500)
    def __str__(self):
        return self.name




