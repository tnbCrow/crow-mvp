from rest_framework import viewsets, mixins, filters

from ..models.completed_trade import CompletedTrade
from ..serializers.recent_trade import RecentTradeSerializer


class RecentTradeViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    """
    ViewSet for Recent Trades.
    """
    queryset = CompletedTrade.objects.all().order_by('-created_at')
    serializer_class = RecentTradeSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['rate', 'created_at']
