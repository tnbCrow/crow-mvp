from django.urls import path, include

from rest_framework.routers import SimpleRouter

from .views import Home, BlacklistedWallets, StatisticViewSet

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('blacklists', BlacklistedWallets.as_view(), name="blacklistedaccounts")
]

router = SimpleRouter(trailing_slash=False)
router.register('statistics', StatisticViewSet)