from django.db import models

from django.db.models.signals import post_save
from django.dispatch import receiver

from .completed_trade import CompletedTrade


class Statistic(models.Model):

    total_escrows = models.IntegerField()
    total_coins = models.IntegerField()
    total_transactions = models.IntegerField()
    weighted_rate = models.IntegerField()
    last_rate = models.IntegerField()
    max_supply = models.IntegerField(default=0)
    circulating_supply = models.IntegerField(default=0)

    api_key = models.CharField(max_length=255)

    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Trades:{self.total_escrows}, Coins:{self.total_coins}, Rate:{self.weighted_rate}'


class BackupStatistic(models.Model):
    total_escrows = models.IntegerField()
    total_coins = models.IntegerField()
    total_transactions = models.IntegerField()
    weighted_rate = models.IntegerField()
    last_rate = models.IntegerField()

    def __str__(self):
        return f'Trades:{self.total_escrows}, Coins:{self.total_coins}, Rate:{self.weighted_rate}'


@receiver(post_save, sender=CompletedTrade)
def save_statistics(sender, instance, created, **kwargs):

    if created:
        total_coins = 0
        transaction = 0

        stat = Statistic.objects.first()
        completed_trades = CompletedTrade.objects.all().order_by('-created_at')[:20]
        for trades in completed_trades:
            transaction += (trades.rate * trades.amount)
            total_coins += trades.amount

        weighted_rate = transaction / total_coins
        stat.total_escrows += 1
        stat.total_coins += instance.amount
        stat.total_transactions += instance.amount * instance.rate / 10000
        stat.weighted_rate = weighted_rate
        stat.last_rate = instance.rate
        BackupStatistic.objects.create(total_escrows=stat.total_escrows,
                                       total_coins=stat.total_coins,
                                       total_transactions=stat.total_transactions,
                                       weighted_rate=stat.weighted_rate,
                                       last_rate=stat.last_rate)
        stat.save()
