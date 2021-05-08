from rest_framework import serializers

from .models import Statistic, CompletedTrade


class StatisticSerializer(serializers.ModelSerializer):

    class Meta:
        model = Statistic
        fields = ('__all__')


class RecentTradeSerializer(serializers.ModelSerializer):
    agent = serializers.CharField(source='agent.discord_username', read_only=True)

    class Meta:
        model = CompletedTrade
        fields = ('uuid', 'agent', 'amount', 'rate', 'created_at')