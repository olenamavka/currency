from django.core.cache import cache
from django.db.models.signals import post_save
from django.dispatch import receiver
from currency import constants
from currency.models import Rate


@receiver(post_save, sender=Rate)
def rate_create_delete(sender, instance, created, **kwargs):
    if created:
        cache.delete(constants.LATEST_RATE_CACHE_KEY)
