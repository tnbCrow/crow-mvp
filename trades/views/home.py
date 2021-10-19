from django.shortcuts import render
from django.views import generic

from ..models.completed_trade import CompletedTrade
from ..models.statistic import Statistic


# Create your views here.
class Home(generic.ListView):
    template_name = 'home.html'

    def get_queryset(self):
        trades = CompletedTrade.objects.all().order_by('-created_at')[:8]
        stats = Statistic.objects.first()
        all_trades = CompletedTrade.objects.all().order_by('created_at')

        query_set = {
            'trades': trades,
            'stats': stats,
            'all_trades': all_trades,
        }
        return query_set


def about_us(request):
    return render(request, 'about_us.html')


def legal(request):
    return render(request, 'legal.html')
