from celery import shared_task
from django.conf import settings
from currency.choices import RateCurrencyChoices
import requests
from bs4 import BeautifulSoup
from currency.constants import PRIVATBANK_CODE_NAME, MONOBANK_CODE_NAME, RATE_SOURCE_CODE_NAME
from currency.utils import to_2_places_decimal


@shared_task
def parse_privatbank():
    from currency.models import Rate, Source

    # source = Source.objects.filter(code_name=PRIVATBANK_CODE_NAME).first()
    #
    # if source is None:
    #     source = Source.objects.create(code_name=PRIVATBANK_CODE_NAME, name='PrivatBank')

    url = 'https://api.privatbank.ua/p24api/pubinfo?exchange&json&coursid=11'

    source, _ = Source.objects.get_or_create(
        code_name=PRIVATBANK_CODE_NAME,
        defaults={
            'name': 'PrivatBank',
            'source_url': url,
        }
    )

    response = requests.get(url)
    response.raise_for_status()
    rates = response.json()

    available_currency = {
        'USD': RateCurrencyChoices.USD,
        'EUR': RateCurrencyChoices.EUR
    }

    for rate in rates:
        if rate['ccy'] not in available_currency:
            continue

        buy = to_2_places_decimal(rate['buy'])
        sale = to_2_places_decimal(rate['sale'])
        currency = rate['ccy']

        last_rate = Rate.objects.filter(
            currency=available_currency[currency],
            source=source
        ).\
            order_by('-created').\
            first()

        if last_rate is None or last_rate.buy != buy or last_rate.sale != sale:
            Rate.objects.create(
                buy=buy,
                sale=sale,
                currency=available_currency[currency],
                source=source
            )


@shared_task
def parse_monobank():
    from currency.models import Rate, Source

    url = 'https://api.monobank.ua/bank/currency'

    source, _ = Source.objects.get_or_create(
        code_name=MONOBANK_CODE_NAME,
        defaults={
            'name': 'Monobank',
            'source_url': url
        }
    )

    response = requests.get(url)
    response.raise_for_status()
    rates = response.json()

    available_currency = {
        840: RateCurrencyChoices.USD,
        978: RateCurrencyChoices.EUR
    }

    for rate in rates:
        if rate['currencyCodeA'] not in available_currency or rate['currencyCodeB'] != 980:
            continue

        buy = to_2_places_decimal(rate['rateBuy'])
        sale = to_2_places_decimal(rate['rateSell'])
        currency = rate['currencyCodeA']

        last_rate = Rate.objects.filter(
            currency=available_currency[currency],
            source=source
        ).\
            order_by('-created').\
            first()

        if last_rate is None or last_rate.buy != buy or last_rate.sale != sale:
            Rate.objects.create(
                buy=buy,
                sale=sale,
                currency=available_currency[currency],
                source=source
            )


@shared_task
def parse_rate():
    from currency.models import Rate, Source

    url = 'https://rate.in.ua/'

    source, _ = Source.objects.get_or_create(
        code_name=RATE_SOURCE_CODE_NAME,
        defaults={
            'name': 'Rate.in.ua',
            'source_url': url
        }
    )

    response = requests.get(url)
    response.raise_for_status()

    available_currency = {
        'USD': RateCurrencyChoices.USD,
        'EUR': RateCurrencyChoices.EUR,
        'GBP': RateCurrencyChoices.GBP
    }

    soup = BeautifulSoup(response.text, 'html.parser')

    rate_table = soup.find('table', class_="summary-exchange-rates")

    for data in rate_table.find_all('tbody'):
        rows = data.find_all('tr')
        for row in rows:
            currency = row.find_all('td')[0].text
            if currency not in available_currency:
                continue

            buy = to_2_places_decimal(row.find_all('td')[1].text)
            sale = to_2_places_decimal(row.find_all('td')[2].text)

            last_rate = Rate.objects.filter(
                currency=available_currency[currency],
                source=source
            ).\
                order_by('-created').\
                first()

            if last_rate is None or last_rate.buy != buy or last_rate.sale != sale:
                Rate.objects.create(
                    buy=buy,
                    sale=sale,
                    currency=available_currency[currency],
                    source=source
                )


@shared_task
def send_mail(subject, message):
    recipient = settings.DEFAULT_FROM_EMAIL
    from django.core.mail import send_mail
    from time import sleep
    sleep(10)
    send_mail(
        subject,
        message,
        recipient,
        [recipient],
        fail_silently=False,
    )
