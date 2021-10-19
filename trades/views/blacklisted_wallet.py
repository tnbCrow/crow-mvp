from django.views import generic

from ..models.blacklisted_wallet import BlacklistedWallet


class BlacklistedWalletViewSet(generic.ListView):
    template_name = 'blacklisted_wallets.html'

    def get_queryset(self):
        wallets = BlacklistedWallet.objects.all().order_by('-created_at')[:20]

        query_set = {
            'wallets': wallets,
        }
        return query_set
