from django.db import models
from wallets.models import Wallet

class Operation(models.Model):
    wallet = models.ForeignKey(Wallet, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField(null=True, blank=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    direction = models.CharField(max_length=10, choices=[('income', 'Income'), ('expense', 'Expense')])
    description = models.TextField()

    def __str__(self):
        return f"{self.direction} - {self.amount}"