from django.urls import path

from rest_framework.routers import SimpleRouter

from .views.home import Home, about_us, legal
from .views.blacklisted_wallet import BlacklistedWalletViewSet
from .views.statistic import StatisticViewSet
from .views.recent_trade import RecentTradeViewSet
from .views.market_chart import MarketChartViewSet


urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('blacklists', BlacklistedWalletViewSet.as_view(), name="blacklistedaccounts"),
    path('about', about_us, name='aboutus'),
    path('legal-disclaimer', legal, name='legal-disclaimer')
]

router = SimpleRouter(trailing_slash=False)
router.register('statistics', StatisticViewSet)
router.register('recent-trades', RecentTradeViewSet)
router.register('market-chart', MarketChartViewSet)
