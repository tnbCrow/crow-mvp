from django.db import models

# Create your models here.
class CompletedTrades(models.Model):
    buyer = models.CharField(max_length=63)
    seller = models.CharField(max_length=63)
    amount = models.PositiveBigIntegerField()
    rate = models.IntegerField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.buyer}-{self.seller}:{self.amount}@{self.rate}'
    