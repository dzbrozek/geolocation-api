# Routers provide an easy way of automatically determining the URL conf.
from rest_framework import routers

from geolocations.views import GeolocationRequestViewSet

app_name = 'geolocations'

router = routers.DefaultRouter()
router.register(r'geolocations', GeolocationRequestViewSet, basename='geolocation')

urlpatterns = router.urls
