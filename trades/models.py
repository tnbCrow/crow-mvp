from uuid import uuid4

from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class CompletedTrade(models.Model):
    uuid = models.UUIDField(default=uuid4, editable=False, primary_key=True)
    buyer = models.CharField(max_length=63)
    seller = models.CharField(max_length=63)
    agent = models.CharField(max_length=63)
    amount = models.PositiveIntegerField()
    rate = models.IntegerField()
    
    buyer_public = models.BooleanField(default=False)
    seller_public = models.BooleanField(default=False)
    agent_public = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.buyer}-{self.seller}:{self.amount}@{self.rate}'


class Statistic(models.Model):
    total_escrows = models.IntegerField()
    total_coins = models.IntegerField()
    total_transactions = models.IntegerField()
    rate = models.IntegerField()

    def __str__(self):
        return f'Trades:{self.total_escrows}, Coins:{self.total_coins}, Rate:{self.rate}'

@receiver(post_save, sender=CompletedTrade)
def save_statistics(sender, instance, created, **kwargs):
    
    if created:
        total_coins = 0
        transaction = 0
        
        stat = Statistic.objects.get(id=1)
        completed_trades = CompletedTrade.objects.all().order_by('-created_at')[:20]
        for trades in completed_trades:
            transaction += (trades.rate * trades.amount)
            total_coins += trades.amount

        weighted_rate = transaction / total_coins
        stat.total_escrows += 1
        stat.total_coins += instance.amount
        stat.total_transactions += instance.amount * instance.rate / 10000
        stat.rate = weighted_rate
        stat.save()