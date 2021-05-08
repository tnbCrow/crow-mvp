from rest_framework import serializers

from .models import Statistic, CompletedTrade


class StatisticSerializer(serializers.ModelSerializer):

    class Meta:
        model = Statistic
        fields = ('__all__')


class RecentTradeSerializer(serializers.ModelSerializer):
    escrower = serializers.CharField(source='escrower.discord_username', read_only=True)

    class Meta:
        model = CompletedTrade
        fields = ('uuid', 'escrower', 'amount', 'rate', 'created_at')