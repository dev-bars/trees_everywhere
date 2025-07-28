from django.db import models 
from django.contrib.auth.models import User


class Account(models.Model):
    name = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)
    users = models.ManyToManyField(User, related_name='accounts')

    def __str__(self):
        return self.name

from decimal import Decimal

class Tree(models.Model):
    name = models.CharField(max_length=100)
    scientific_name = models.CharField(max_length=150, blank=True, null=True)

    def __str__(self):
        return self.name

class PlantedTree(models.Model):
    tree = models.ForeignKey(Tree, on_delete=models.CASCADE, related_name='plantings')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    age = models.PositiveIntegerField(default=0)  # idade da árvore em anos
    planted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.tree.name} planted by {self.user.username}"


