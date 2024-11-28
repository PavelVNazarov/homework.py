from django.db import models

class Product(models.Model):
    id = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    url = models.CharField(max_length=100)
    short_name = models.TextField(max_length=100)

    def __str__(self):
        return self.name

