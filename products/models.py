from django.db import models
from django.urls import reverse

# Create your models here.


class Product(models.Model):
    """
    Model for products
    """
    EXTRA_COARSE = 'Extra Coarse'
    COARSE = 'Coarse'
    MEDIUM_COARSE = 'Medium Coarse'
    MEDIUM = 'Medium'
    MEDIUM_FINE = 'Medium Fine'
    FINE = 'Fine'
    VERY_FINE = 'Very Fine'
    GRIND_OPTIONS = [
        (EXTRA_COARSE, 'Extra Coarse'),
        (COARSE, 'Coarse'),
        (MEDIUM_COARSE, 'Medium Coarse'),
        (MEDIUM, 'Medium'),
        (MEDIUM_FINE, 'Medium Fine'),
        (FINE, 'Fine'),
        (VERY_FINE, 'Very Fine'),
    ]
    name = models.CharField(max_length=254, default='')
    grind_size = models.CharField(
        max_length=20,
        choices=GRIND_OPTIONS,
        default=FINE,
    )
    excerpt = models.TextField(max_length=30, default='some string')
    description = models.TextField(default='some string')
    description2 = models.TextField(default='some string')
    promoted = models.BooleanField(default=False)
    image = models.ImageField(upload_to='static/images')
    price = models.DecimalField(max_digits=6, decimal_places=2)
    recommended_retail_price = models.DecimalField(max_digits=6, decimal_places=2, default=0.0)

    def __str__(self):
        return self.name
