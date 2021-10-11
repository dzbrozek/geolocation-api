from django.contrib import admin

from geolocations.models import Geolocation, GeolocationRequest


@admin.register(GeolocationRequest)
class GeolocationRequestAdmin(admin.ModelAdmin):
    list_display = ('id', 'lookup', 'user', 'created_at')
    search_fields = ('id', 'lookup')
    list_filter = ('created_at',)
    raw_id_fields = ('user',)


@admin.register(Geolocation)
class GeolocationAdmin(admin.ModelAdmin):
    list_display = ('id', 'ip', 'type', 'city', 'zip', 'latitude', 'longitude')
    search_fields = ('id', 'ip', 'city', 'zip')
    list_filter = ('type',)
    raw_id_fields = ('request',)
