from django.urls import path

from currency.views import (
    RateListView,
    RateCreateView,
    RateDetailView,
    RateUpdateView,
    RateDeleteView,
    ContactUsListView,
    ContactUsCreateView,
    ContactUsDetailView,
    ContactUsUpdateView,
    ContactUsDeleteView,
    SourceListView,
    SourceCreateView,
    SourceDetailView,
    SourceUpdateView,
    SourceDeleteView
)


app_name = 'currency'


urlpatterns = [
    path('rate/list/', RateListView.as_view(), name='rate-list'),
    path('rate/create/', RateCreateView.as_view(), name='rate-create'),
    path('rate/details/<int:pk>/', RateDetailView.as_view(), name='rate-details'),
    path('rate/update/<int:pk>/', RateUpdateView.as_view(), name='rate-update'),
    path('rate/delete/<int:pk>/', RateDeleteView.as_view(), name='rate-delete'),
    path('contact-us/list/', ContactUsListView.as_view(), name='contact-us-list'),
    path('contact-us/create/', ContactUsCreateView.as_view(), name='contact-us-create'),
    path('contact-us/details/<int:pk>/', ContactUsDetailView.as_view(), name='contact-us-details'),
    path('contact-us/update/<int:pk>/', ContactUsUpdateView.as_view(), name='contact-us-update'),
    path('contact-us/delete/<int:pk>/', ContactUsDeleteView.as_view(), name='contact-us-delete'),
    path('source/list/', SourceListView.as_view(), name='source-list'),
    path('source/create/', SourceCreateView.as_view(), name='source-create'),
    path('source/details/<int:pk>/', SourceDetailView.as_view(), name='source-details'),
    path('source/update/<int:pk>/', SourceUpdateView.as_view(), name='source-update'),
    path('source/delete/<int:pk>/', SourceDeleteView.as_view(), name='source-delete'),
]
