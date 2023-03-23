from django.contrib import admin
from django.urls import path, include
from currency.views import IndexView, ProfileView


urlpatterns = [
    path('admin/', admin.site.urls),

    path('auth/', include('django.contrib.auth.urls')),
    path('profile/', ProfileView.as_view(), name='profile'),

    path('__debug__/', include('debug_toolbar.urls')),

    path('', IndexView.as_view(), name='index'),

    path('currency/', include('currency.urls'))
]
