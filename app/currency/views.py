from django.http import HttpResponse

from currency.models import Rate, ContactUs
from django.shortcuts import render


def list_rates(request):
    rates = Rate.objects.all()

    context = {
        'rates': rates
    }

    return render(request, 'rates_list.html', context)


def list_contact_us(request):
    contact_us = ContactUs.objects.all()

    context = {
        'contact_us': contact_us
    }

    return render(request, 'contact_us.html', context)


def status_code(request):
    # create user

    response = HttpResponse(
        'Not Found',
        status=404,
    )
    return response
