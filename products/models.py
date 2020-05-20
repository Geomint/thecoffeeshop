from django.db import models
from django.urls import reverse

# Create your models here.

class Product(models.Model):
    """
    Model for products
    """
    name = models.CharField(max_length=254, default='')
    grind_size = models.CharField(max_length=30, default='')
    description = models.TextField()
    image = models.ImageField(upload_to='images')
    price = models.DecimalField(max_digits=6, decimal_places=2)
    
    def __str__(self):
        return self.name