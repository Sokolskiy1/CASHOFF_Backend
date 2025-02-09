from django.db import models
from django.contrib.auth.models import User

class Wallet(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    balance = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.CharField(max_length=10)

    def __str__(self):
        return self.name