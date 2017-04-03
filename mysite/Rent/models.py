from django.db import models


# Create your models here.
class Bounce(models.Model):
    name = models.CharField(max_length=30)
    image = models.CharField(max_length=150, default=0)
    quantity = models.IntegerField()
    price = models.IntegerField()
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class ShoppingCart(models.Model):
    name = models.CharField(max_length=30)
    price = models.IntegerField()

    def __str__(self):
        return self.name
