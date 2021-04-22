from django.shortcuts import render
from django.views import generic

from .models import CompletedTrade, Statistic, BlacklistedWallet

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
