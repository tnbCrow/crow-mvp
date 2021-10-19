from rest_framework import serializers

from ..models.completed_trade import CompletedTrade


class RecentTradeSerializer(serializers.ModelSerializer):

    class Meta:
        model = CompletedTrade
        fields = ('uuid', 'amount', 'rate', 'created_at')
