from django.urls import path, include

from rest_framework.routers import SimpleRouter

from .views import Home, BlacklistedWallets, StatisticViewSet, RecentTradeViewSet, about_us, legal

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('blacklists', BlacklistedWallets.as_view(), name="blacklistedaccounts"),
    path('about', about_us, name='aboutus'),
    path('legal-disclaimer', legal, name='legal-disclaimer')
]

router = SimpleRouter(trailing_slash=False)
router.register('statistics', StatisticViewSet)
router.register('recent-trades', RecentTradeViewSet)
