# Routers provide an easy way of automatically determining the URL conf.
from geolocations.views import GeolocationRequestViewSet
from rest_framework import routers

app_name = 'geolocations'

router = routers.DefaultRouter()
router.register(r'geolocations', GeolocationRequestViewSet, basename='geolocation')

urlpatterns = router.urls
