from rest_framework.routers import DefaultRouter

from currency.api.v1.views import RateViewSet, SourceViewSet, ContactUsViewSet

app_name = 'api-currency'

router = DefaultRouter()
router.register(r'rates', RateViewSet, basename='rates')
router.register(r'contact-us', ContactUsViewSet, basename='contact-us')
router.register(r'source', SourceViewSet, basename='source')

urlpatterns = [
    # path('rates/', RateApiView.as_view(), name='rates-list'),
    # path('rates/<int:pk>/', RateDetailApiView.as_view(), name='rates-detail')
]

urlpatterns += router.urls
