from rest_framework import viewsets

from ..models.statistic import Statistic
from ..serializers.statistic import StatisticSerializer


class StatisticViewSet(viewsets.ReadOnlyModelViewSet):
    """
    ViewSet for Statistic.
    """
    queryset = Statistic.objects.all()
    serializer_class = StatisticSerializer
