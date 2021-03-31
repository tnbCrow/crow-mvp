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
    amount = models.PositiveBigIntegerField()
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
    rate = models.IntegerField()

    def __str__(self):
        return f'Trades:{self.total_escrows}, Coins:{self.total_coins}, Rate:{self.rate}'

@receiver(post_save, sender=CompletedTrade)
def save_statistics(sender, instance, created, **kwargs):
    
    if created:
        stat = Statistic.objects.get(id=1)
        weighted_rate = (stat.rate * stat.total_coins + instance.rate * instance.amount ) / ( stat.total_coins + instance.amount)
        stat.total_escrows += 1
        stat.total_coins += instance.amount
        stat.rate = weighted_rate
        stat.save()