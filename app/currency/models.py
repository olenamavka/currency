from django.db import models
from django.utils import timezone

from currency.choices import RateCurrencyChoices


class Rate(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    currency = models.PositiveSmallIntegerField(
        choices=RateCurrencyChoices.choices,
        default=RateCurrencyChoices.USD
    )
    buy = models.DecimalField(max_digits=6, decimal_places=2)
    sell = models.DecimalField(max_digits=6, decimal_places=2)
    # source = models.CharField(max_length=25)
    source = models.ForeignKey('currency.Source', on_delete=models.CASCADE, related_name='rates')

    def __str__(self):
        return f'Currency: {self.get_currency_display()}, Buy: {self.buy}'


class ContactUs(models.Model):
    created = models.DateTimeField(default=timezone.now)
    name = models.CharField(max_length=128, default='')
    email_from = models.EmailField(max_length=40)
    subject = models.CharField(max_length=256)
    message = models.TextField()

    def __str__(self):
        return f'Email from: {self.email_from}, Subject: {self.subject}'


class Source(models.Model):
    source_url = models.URLField(max_length=255)
    name = models.CharField(max_length=64)
    number = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return self.name


class RequestResponseLog(models.Model):
    path = models.CharField(max_length=128)
    request_method = models.CharField(max_length=32)
    time = models.FloatField()
