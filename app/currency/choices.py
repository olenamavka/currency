# CURRENCY_EUR = 1
# CURRENCY_USD = 2
#
# CURRENCY_TYPE = [
#     (CURRENCY_USD, 'Dollar'),
#     (CURRENCY_EUR, 'Euro'),
# ]
from django.db import models


class RateCurrencyChoices(models.IntegerChoices):
    EUR = 1, 'Euro'
    USD = 2, 'Dollar'
    GBP = 3, 'Sterling'
