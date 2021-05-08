from django.contrib import admin
from .models import CompletedTrade, Statistic, BackupStatistic, BlacklistedWallet, Agent

# Register your models here.
admin.site.register(CompletedTrade)
admin.site.register(Statistic)
admin.site.register(BackupStatistic)
admin.site.register(BlacklistedWallet)
admin.site.register(Agent)
