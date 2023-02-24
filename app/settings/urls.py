from django.contrib import admin
from django.urls import path

from currency.views import list_rates, list_contact_us, status_code


urlpatterns = [
    path('admin/', admin.site.urls),
    path('rate/list/', list_rates),
    path('contact-us/', list_contact_us),
    path('status1/', status_code)
]
