from rest_framework import views, viewsets, mixins, filters, generics

from ..models.completed_trade import CompletedTrade
from ..serializers.recent_trade import RecentTradeSerializer


class RecentTradeViewSet(generics.ListCreateAPIView,
                         viewsets.GenericViewSet):

    queryset = CompletedTrade.objects.all().order_by('-created_at')
    serializer_class = RecentTradeSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['rate', 'created_at']
