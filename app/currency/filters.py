import django_filters

from currency.models import Rate, ContactUs, Source


class RateFilter(django_filters.FilterSet):

    class Meta:
        model = Rate
        # fields = ['buy', 'sale']
        fields = {
            'buy': ('gt', 'gte', 'lt', 'lte', 'exact'),
            'sale': ('gt', 'gte', 'lt', 'lte', 'exact'),
        }


class ContactUsFilter(django_filters.FilterSet):

    class Meta:
        model = ContactUs
        # fields = ['name', 'subject']
        fields = {
            'name': ('contains', 'startswith', 'endswith', 'exact'),
            'subject': ('contains', 'startswith', 'endswith', 'exact'),
        }


class SourceFilter(django_filters.FilterSet):

    class Meta:
        model = Source
        # fields = ['name']
        fields = {
            'name': ('contains', 'startswith', 'endswith', 'exact'),
        }
