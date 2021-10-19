from django.contrib import admin

from .models.agent import Agent
from .models.completed_trade import CompletedTrade
from .models.statistic import Statistic, BackupStatistic
from .models.blacklisted_wallet import BlacklistedWallet


# Register your models here.
admin.site.register(CompletedTrade)
admin.site.register(Statistic)
admin.site.register(BackupStatistic)
admin.site.register(BlacklistedWallet)
admin.site.register(Agent)
