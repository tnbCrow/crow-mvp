from rest_framework import serializers

from ..models.statistic import Statistic


class StatisticSerializer(serializers.ModelSerializer):

    class Meta:
        model = Statistic
        fields = ('__all__')
