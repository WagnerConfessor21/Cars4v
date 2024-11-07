from django.db import models

class Car(models.Model):
    model = models.CharField(max_length=50, null=False)
    brand = models.CharField(max_length=50, null=False)
    year = models.IntegerField(null=False)
    filename = models.CharField(max_length=50, null=False)
# Create your models here.
