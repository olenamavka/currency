from currency.models import Rate, ContactUs, Source
from currency.forms import RateForm, SourceForm, ContactUsForm
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView, TemplateView


class RateListView(ListView):
    template_name = 'rates_list.html'
    queryset = Rate.objects.all()


class RateDetailView(DetailView):
    queryset = Rate.objects.all()
    template_name = 'rates_details.html'


class RateCreateView(CreateView):
    form_class = RateForm
    template_name = 'rates_create.html'
    success_url = reverse_lazy('currency:rate-list')


class RateUpdateView(UpdateView):
    form_class = RateForm
    template_name = 'rates_update.html'
    success_url = reverse_lazy('currency:rate-list')
    queryset = Rate.objects.all()


class RateDeleteView(DeleteView):
    queryset = Rate.objects.all()
    template_name = 'rates_delete.html'
    success_url = reverse_lazy('currency:rate-list')


class ContactUsListView(ListView):
    template_name = 'contact_us_list.html'
    queryset = ContactUs.objects.all()


class ContactUsDetailView(DetailView):
    queryset = ContactUs.objects.all()
    template_name = 'contact_us_details.html'


class ContactUsCreateView(CreateView):
    form_class = ContactUsForm
    template_name = 'contact_us_create.html'
    success_url = reverse_lazy('currency:contact-us-list')


class ContactUsUpdateView(UpdateView):
    form_class = ContactUsForm
    template_name = 'contact_us_update.html'
    success_url = reverse_lazy('currency:contact-us-list')
    queryset = ContactUs.objects.all()


class ContactUsDeleteView(DeleteView):
    queryset = ContactUs.objects.all()
    template_name = 'contact_us_delete.html'
    success_url = reverse_lazy('currency:contact-us-list')


class SourceListView(ListView):
    template_name = 'source_list.html'
    queryset = Source.objects.all()


class SourceDetailView(DetailView):
    queryset = Source.objects.all()
    template_name = 'source_details.html'


class SourceCreateView(CreateView):
    form_class = SourceForm
    template_name = 'source_create.html'
    success_url = reverse_lazy('currency:source-list')


class SourceUpdateView(UpdateView):
    form_class = SourceForm
    template_name = 'source_update.html'
    success_url = reverse_lazy('currency:source-list')
    queryset = Source.objects.all()


class SourceDeleteView(DeleteView):
    queryset = Source.objects.all()
    template_name = 'source_delete.html'
    success_url = reverse_lazy('currency:source-list')


class IndexView(TemplateView):
    template_name = 'index.html'
