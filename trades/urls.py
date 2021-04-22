from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('blacklists', views.BlacklistedWallets.as_view(), name="blacklistedaccounts")
]