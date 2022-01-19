from rest_framework import views, viewsets, mixins, filters, generics
from rest_framework.pagination import LimitOffsetPagination

from ..models.completed_trade import CompletedTrade
from ..serializers.market_chart import MarketChartSerializer


class MarketChartViewSet(generics.ListAPIView,
                         viewsets.GenericViewSet):

    queryset = CompletedTrade.objects.all().order_by('created_at')
    serializer_class = MarketChartSerializer
