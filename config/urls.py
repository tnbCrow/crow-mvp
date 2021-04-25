from django.contrib import admin
from django.urls import path, include

from rest_framework.routers import DefaultRouter

from trades.urls import router as trades_router

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('trades.urls'))
]

router = DefaultRouter(trailing_slash=False)
router.registry.extend(trades_router.registry)
urlpatterns += router.urls
