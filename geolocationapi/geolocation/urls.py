# Routers provide an easy way of automatically determining the URL conf.
from geolocation.views import GeolocationRequestViewSet
from rest_framework import routers

app_name = 'geolocation'

router = routers.DefaultRouter()
router.register(r'geolocation', GeolocationRequestViewSet, basename='geolocation')

urlpatterns = router.urls
