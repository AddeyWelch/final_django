from django.db import models


# Create your models here.
class Bounce(models.Model):
    name = models.CharField(max_length=30)
    quantity = models.IntegerField()
    price = models.IntegerField()
    description = models.CharField(max_length=100)
