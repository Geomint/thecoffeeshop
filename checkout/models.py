from django.db import models
from products.models import Product
from django.contrib.auth.models import User


# Create your models here.


class Order(models.Model):
    """
    This is the order model to create an order instance in the database
    """
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    full_name = models.CharField(max_length=50, blank=False)
    phone_number = models.CharField(max_length=20, blank=False)
    country = models.CharField(max_length=40, blank=False)
    postcode = models.CharField(max_length=40, blank=False)
    city = models.CharField(max_length=40, blank=False)
    address_line_1 = models.CharField(max_length=40, blank=False)
    address_line_2 = models.CharField(max_length=40, blank=False)
    date = models.DateField()

    def __str__(self):
        return f'{self.id}-{self.date}-{self.user.id}'

class OrderItem(models.Model):
    """
    This is the orderitem model to create an orderitem instance in the database
    """
    order = models.ForeignKey(Order, null=False)
    product = models.ForeignKey(Product, null=False)
    quantity = models.IntegerField(blank=False)

    def __str__(self):
        return f'{self.quantity}-{self.product.name}'


