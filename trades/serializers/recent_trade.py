from rest_framework import serializers

from trades.models.statistic import Statistic

from ..models.completed_trade import CompletedTrade


class RecentTradeSerializer(serializers.ModelSerializer):

    api_key = serializers.CharField(max_length=255, write_only=True)

    class Meta:
        model = CompletedTrade
        fields = ('uuid', 'amount', 'rate', 'api_key', 'created_at')
        read_only_fields = 'uuid', 'created_at'
    
    def validate(self, attrs):

        api_key = attrs.pop("api_key")

        if not Statistic.objects.filter(api_key=api_key).exists():
            error = {'error': 'Invalid API Key.'}
            raise serializers.ValidationError(error)

        return super().validate(attrs)