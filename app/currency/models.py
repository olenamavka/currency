from django.db import models

from currency.choices import RateCurrencyChoices


class Rate(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    currency = models.PositiveSmallIntegerField(
        choices=RateCurrencyChoices.choices,
        default=RateCurrencyChoices.USD
    )
    buy = models.DecimalField(max_digits=6, decimal_places=2)
    sell = models.DecimalField(max_digits=6, decimal_places=2)
    source = models.CharField(max_length=25)

    def __str__(self):
        return f'Currency: {self.get_currency_display()}, Buy: {self.buy}'


class ContactUs(models.Model):
    email_from = models.EmailField(max_length=40)
    subject = models.CharField(max_length=100)
    message = models.TextField()

    def __str__(self):
        return f'Email from: {self.email_from}, Subject: {self.subject}'


class Source(models.Model):
    source_url = models.URLField(max_length=255)
    name = models.CharField(max_length=64)
    number = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return f'Source URL: {self.source_url}, Name: {self.name}'
