from django.shortcuts import render
from django.views import generic

from .models import CompletedTrade, Statistic

# Create your views here.
class Home(generic.ListView):
    template_name = 'home.html'

    def get_queryset(self):
        trades = CompletedTrade.objects.all()[:8]
        stats = Statistic.objects.get(id=1)

        query_set = {
            'trades' : trades,
            'stats' : stats,
        }
        return query_set