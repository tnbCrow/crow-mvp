from uuid import uuid4

from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class Agent(models.Model):

    discord_username = models.CharField(max_length=37)
    github_username = models.CharField(max_length=39, blank=True, null=True)
    twitter_username = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return self.discord_username


class CompletedTrade(models.Model):
    uuid = models.UUIDField(default=uuid4, editable=False, primary_key=True)
    buyer = models.CharField(max_length=63)
    seller = models.CharField(max_length=63)
    agent = models.CharField(max_length=63)
    escrower = models.ForeignKey(Agent, on_delete=models.CASCADE)
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
    weighted_rate = models.IntegerField()
    last_rate = models.IntegerField()

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


class BlacklistedWallet(models.Model):
    account_number = models.CharField(max_length=64)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.account_number


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
        stat.weighted_rate = weighted_rate
        stat.last_rate = instance.rate
        BackupStatistic.objects.create(total_escrows = stat.total_escrows,
                                       total_coins = stat.total_coins,
                                       total_transactions = stat.total_transactions,
                                       weighted_rate = stat.weighted_rate,
                                       last_rate = stat.last_rate)
        stat.save()
