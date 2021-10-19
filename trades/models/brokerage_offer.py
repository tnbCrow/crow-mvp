import uuid

from django.db import models


class BrokerageOffer(models.Model):

    NEW = 'NEW'
    FILLED = 'FILLED'
    PARTIALLY_FILLED = 'PARTIALLY_FILLED'
    CANCELLED = 'CANCELLED'

    BUY = 'BUY'
    SELL = 'SELL'

    status_choices = [
        (NEW, 'New'),
        (FILLED, 'Filled'),
        (PARTIALLY_FILLED, 'Partially Filled'),
        (CANCELLED, 'Cancelled'),
    ]

    side_choices = [
        (BUY, 'Buy'),
        (SELL, 'Sell')
    ]

    uuid = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    uuid_hex = models.CharField(max_length=255, unique=True)

    amount = models.IntegerField()  # TNBC Amount
    executed = models.IntegerField(default=0)  # TNBC executed
    price = models.IntegerField()  # price per TNBC | in 10 ^ 4
    total = models.IntegerField()  # BUSD Value

    status = models.CharField(max_length=255, choices=status_choices, default='NEW')
    side = models.CharField(max_length=255, choices=side_choices)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


# generate a random uuid_hex and check if its already taken.
# If taken, generate another uuid_hex again until we find a valid memo
def generate_hex_uuid(instance):

    while True:

        uuid_hex = f'{uuid.uuid4().hex}'

        if not BrokerageOffer.objects.filter(uuid_hex=uuid_hex).exists():
            return uuid_hex


def pre_save_post_receiver(sender, instance, *args, **kwargs):

    if not instance.uuid_hex:
        instance.uuid_hex = generate_hex_uuid(instance)


# save the memo before the User model is saved with the unique memo
models.signals.pre_save.connect(pre_save_post_receiver, sender=BrokerageOffer)
