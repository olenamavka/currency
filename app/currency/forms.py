from django import forms

from currency.models import Rate, Source, ContactUs


class RateForm(forms.ModelForm):
    class Meta:
        model = Rate
        fields = (
            'buy',
            'sale',
            'source',
            'currency'
        )


class ContactUsForm(forms.ModelForm):
    class Meta:
        model = ContactUs
        fields = (
            'name',
            'email_from',
            'subject',
            'message'
        )


class SourceForm(forms.ModelForm):
    class Meta:
        model = Source
        fields = (
            'logo',
            'source_url',
            'name',
            'number'
        )
