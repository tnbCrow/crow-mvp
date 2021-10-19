from rest_framework import serializers

from ..models.brokerage_offer import BrokerageOffer


class BrokerageOfferSerializer(serializers.ModelSerializer):

    class Meta:
        model = BrokerageOffer
        fields = ('uuid', 'uuid_hex', 'amount', 'executed', 'price', 'total', 'status', 'side')
        read_only_fields = 'uuid_hex',
