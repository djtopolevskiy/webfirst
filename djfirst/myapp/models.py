from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField(max_length=20)
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.name
