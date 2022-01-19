from rest_framework import serializers

from ..models.completed_trade import CompletedTrade


class MarketChartSerializer(serializers.ModelSerializer):

    class Meta:
        model = CompletedTrade
        fields = ('rate', 'created_at')
