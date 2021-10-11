from django.db import models


class GeolocationRequest(models.Model):
    lookup = models.CharField(max_length=100)
    user = models.ForeignKey('auth.User', on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Geolocation request: ${self.pk}'


class Geolocation(models.Model):
    request = models.OneToOneField(GeolocationRequest, on_delete=models.CASCADE)
    ip = models.GenericIPAddressField()
    type = models.CharField(max_length=4)
    continent_code = models.CharField(max_length=2, blank=True)
    continent_name = models.CharField(max_length=20, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    country_name = models.CharField(max_length=50, blank=True)
    region_code = models.CharField(max_length=2, blank=True)
    region_name = models.CharField(max_length=50, blank=True)
    city = models.CharField(max_length=50, blank=True)
    zip = models.CharField(max_length=10, blank=True)
    latitude = models.DecimalField(max_digits=20, decimal_places=18, null=True, blank=True)
    longitude = models.DecimalField(max_digits=20, decimal_places=17, null=True, blank=True)

    def __str__(self):
        return f'Geolocation: ${self.pk}'
