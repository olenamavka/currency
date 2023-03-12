from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views.decorators.csrf import csrf_exempt

from currency.models import Rate, ContactUs, Source
from currency.forms import RateForm, SourceForm, ContactUsForm


# GET(list)
def list_rates(request):
    rates = Rate.objects.all()

    context = {
        'rates': rates
    }

    return render(request, 'rates_list.html', context)


# GET(details)
def rates_details(request, pk):
    rate = get_object_or_404(Rate, pk=pk)

    context = {
        'rate': rate
    }

    return render(request, 'rates_details.html', context)


def rates_create(request):
    if request.method == 'POST':
        form = RateForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/rate/list/')
    elif request.method == 'GET':
        form = RateForm()

    context = {
        'form': form
    }
    return render(request, 'rates_create.html', context)


def rates_update(request, pk):
    rate = get_object_or_404(Rate, pk=pk)

    if request.method == 'POST':
        form = RateForm(request.POST, instance=rate)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/rate/list/')
    elif request.method == 'GET':
        form = RateForm(instance=rate)

    context = {
        'form': form
    }
    return render(request, 'rates_update.html', context)


def rates_delete(request, pk):
    rate = get_object_or_404(Rate, pk=pk)

    if request.method == 'POST':
        rate.delete()
        return HttpResponseRedirect('/rate/list/')
    elif request.method == 'GET':
        context = {
            'rate': rate
        }
        return render(request, 'rates_delete.html', context)


def list_contact_us(request):
    contact_us = ContactUs.objects.all()

    context = {
        'contact_us': contact_us
    }

    return render(request, 'contact_us.html', context)


def contact_us_update(request, pk):
    contact = get_object_or_404(ContactUs, pk=pk)

    if request.method == 'POST':
        form = ContactUsForm(request.POST, instance=contact)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/contact-us/')
    elif request.method == 'GET':
        form = ContactUsForm(instance=contact)

    context = {
        'form': form
    }
    return render(request, 'contact_us_update.html', context)


def list_source(request):
    source = Source.objects.all()

    context = {
        'source': source
    }

    return render(request, 'source.html', context)


def source_details(request, pk):
    source = get_object_or_404(Source, pk=pk)

    context = {
        'source': source
    }

    return render(request, 'source_details.html', context)


def source_create(request):
    if request.method == 'POST':
        form = SourceForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/source/')
    elif request.method == 'GET':
        form = SourceForm()

    context = {
        'form': form
    }

    return render(request, 'source_create.html', context)


def source_update(request, pk):
    source = get_object_or_404(Source, pk=pk)

    if request.method == 'POST':
        form = SourceForm(request.POST, instance=source)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/source/')
    elif request.method == 'GET':
        form = SourceForm(instance=source)

    context = {
        'form': form
    }

    return render(request, 'source_update.html', context)


def source_delete(request, pk):
    source = get_object_or_404(Source, pk=pk)

    if request.method == 'POST':
        source.delete()
        return HttpResponseRedirect('/source/')
    elif request.method == 'GET':
        context = {
            'source': source
        }
        return render(request, 'source_delete.html', context)


def status_code(request):
    # create user

    response = HttpResponse(
        'Not Found',
        status=404,
    )
    return response


@csrf_exempt
def request_methods(request):
    if request.method == 'GET':
        message = 'GET method'
    elif request.method == 'POST':
        message = 'POST method'
    return HttpResponse(message)
