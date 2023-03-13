from django.contrib import admin
from django.urls import path

from currency.views import (
    list_rates, rates_create, rates_details, rates_update, rates_delete,
    list_source, source_details, source_create, source_update, source_delete,
    list_contact_us, contact_us_update,
    status_code, request_methods
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('rate/list/', list_rates),
    path('rate/create/', rates_create),
    path('rate/details/<int:pk>/', rates_details),
    path('rate/update/<int:pk>/', rates_update),
    path('rate/delete/<int:pk>/', rates_delete),
    path('contact-us/', list_contact_us),
    path('contact-us/update/<int:pk>/', contact_us_update),
    path('source/', list_source),
    path('source/create/', source_create),
    path('source/details/<int:pk>/', source_details),
    path('source/update/<int:pk>/', source_update),
    path('source/delete/<int:pk>/', source_delete),
    path('status1/', status_code),
    path('rm/', request_methods)
]
