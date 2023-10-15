from django.db import models


class Drink(models.model):
    name = models.charField(max_length=200)
    description = models.charField(max_length=500)
