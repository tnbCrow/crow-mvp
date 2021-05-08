from django.shortcuts import render
from django.views import generic

from rest_framework import viewsets, mixins

from .models import CompletedTrade, Statistic, BlacklistedWallet
from .serializers import StatisticSerializer, RecentTradeSerializer

# Create your views here.
class Home(generic.ListView):
    template_name = 'home.html'

    def get_queryset(self):
        trades = CompletedTrade.objects.all().order_by('-created_at')[:8]
        stats = Statistic.objects.get(id=1)

        query_set = {
            'trades' : trades,
            'stats' : stats,
        }
        return query_set


class BlacklistedWallets(generic.ListView):
    template_name = 'blacklisted_wallets.html'
    
    def get_queryset(self):
        wallets = BlacklistedWallet.objects.all().order_by('-created_at')[:20]

        query_set = {
            'wallets' : wallets,
        }
        return query_set


class StatisticViewSet(viewsets.ReadOnlyModelViewSet):
    """
    ViewSet for Statistic.
    """
    queryset = Statistic.objects.all()
    serializer_class = StatisticSerializer


class RecentTradeViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    """
    ViewSet for Recent Trades.
    """
    queryset = CompletedTrade.objects.all()
    serializer_class = RecentTradeSerializer
