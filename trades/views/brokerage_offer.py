from rest_framework import viewsets, mixins, filters
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny, SAFE_METHODS
from django_filters.rest_framework import DjangoFilterBackend, OrderingFilter

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
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['side', 'status']
    ordering_fields = ['price',]

    def get_permissions(self):
        if self.request.method in SAFE_METHODS:
            return [AllowAny(), ]
        else:
            return [IsAdminUser(), ]
