from rest_framework import viewsets, mixins
from rest_framework.permissions import IsAuthenticated

from ..models.brokerage_offer import BrokerageOffer
from ..serializers.brokerage_offer import BrokerageOfferSerializer


class BrokerageOfferViewSet(mixins.CreateModelMixin,
                            mixins.RetrieveModelMixin,
                            mixins.ListModelMixin,
                            mixins.UpdateModelMixin,
                            viewsets.GenericViewSet):

    '''
    Price in 10 ^ 4 of actual value.
    '''

    queryset = BrokerageOffer.objects.all()
    serializer_class = BrokerageOfferSerializer
    permission_classes = [IsAuthenticated]
