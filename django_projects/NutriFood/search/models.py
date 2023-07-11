from django.db import models

class produits(models.Model):
    ingredients = models.CharField(max_length=100)