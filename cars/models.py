from django.db import models


class Car(models.Model):
    name = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    year = models.PositiveIntegerField()