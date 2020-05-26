from django.db import models

# Create your models here.


class Order(models.Model):
    full_name = models.CharField(max_length=50, blank=False)
    phone_number = models.CharField(max_length=20, blank=False)
    country = models.CharField(max_length=40, blank=False)
    postcode = models.CharField(max_length=40, blank=False)
    city = models.CharField(max_length=40, blank=False)
    address_line_1 = models.CharField(max_length=40, blank=False)
    address_line_2 = models.CharField(max_length=40, blank=False)
    date = models.DateField()

    def __str__(self):
        return f'{self.id}-{self.date}-{self.full_name}'

