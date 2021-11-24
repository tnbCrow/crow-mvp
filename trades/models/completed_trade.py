from uuid import uuid4

from django.db import models

from .agent import Agent


class CompletedTrade(models.Model):
    uuid = models.UUIDField(default=uuid4, editable=False, primary_key=True)
    buyer = models.CharField(max_length=63, null=True, blank=True)
    seller = models.CharField(max_length=63, null=True, blank=True)
    agent = models.ForeignKey(Agent, on_delete=models.CASCADE, null=True, blank=True)
    amount = models.PositiveIntegerField()
    rate = models.IntegerField()

    buyer_public = models.BooleanField(default=False)
    seller_public = models.BooleanField(default=False)
    agent_public = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.buyer}-{self.seller}:{self.amount}@{self.rate}'
