from uuid import uuid4
from django.db import models

# Create your models here.
class CompletedTrade(models.Model):
    uuid = models.UUIDField(default=uuid4, editable=False, primary_key=True)
    buyer = models.CharField(max_length=63)
    seller = models.CharField(max_length=63)
    amount = models.PositiveBigIntegerField()
    rate = models.IntegerField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.buyer}-{self.seller}:{self.amount}@{self.rate}'


class Statistic(models.Model):
    total_escrows = models.IntegerField()
    total_coins = models.IntegerField()
    rate = models.IntegerField()

    def __str__(self):
        return f'Trades:{total_escrows},Coins:{total_coins},Rate:{rate}'
