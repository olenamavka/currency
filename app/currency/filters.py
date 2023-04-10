import django_filters

from currency.models import Rate, ContactUs, Source


class RateFilter(django_filters.FilterSet):

    class Meta:
        model = Rate
        fields = ['buy', 'sale']


class ContactUsFilter(django_filters.FilterSet):

    class Meta:
        model = ContactUs
        fields = ['name', 'subject']


class SourceFilter(django_filters.FilterSet):

    class Meta:
        model = Source
        fields = ['name']
