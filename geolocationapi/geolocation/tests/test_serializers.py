from django.http import HttpRequest
from django.test import TestCase
from django.utils import timezone
from freezegun import freeze_time
from geolocation.factories import UserFactory
from geolocation.serializers import GeolocationRequestSerializer
from rest_framework.exceptions import ErrorDetail


class GeolocationRequestSerializerTest(TestCase):
    def test_invalid_data(self):
        lookups = ("1.1.1", "test")

        for lookup in lookups:
            with self.subTest(f"Testing invalid lookup: {lookup}"):
                data = dict(lookup=lookup)
                serializer = GeolocationRequestSerializer(data=dict(data))

                self.assertFalse(serializer.is_valid())
                self.assertDictEqual(
                    serializer.errors,
                    {'lookup': [ErrorDetail(string='Provide a valid IP address or URL', code='invalid')]},
                )

    def test_ip_address(self):
        lookups = ("19.117.63.126", "684D:1111:222:3333:4444:5555:6:77")

        for lookup in lookups:
            with self.subTest(f"Testing IP address: {lookup}"):
                data = dict(lookup=lookup)
                serializer = GeolocationRequestSerializer(data=dict(data))

                self.assertTrue(serializer.is_valid())

    def test_url(self):
        lookups = (("example.com", "example.com"), ("https://example.com/", "example.com"))

        for input, output in lookups:
            with self.subTest(f"Testing URL: {input}"):
                data = dict(lookup=input)
                serializer = GeolocationRequestSerializer(data=dict(data))

                self.assertTrue(serializer.is_valid())
                self.assertDictEqual(serializer.data, {'lookup': output})

    @freeze_time("2021-10-11")
    def test_create(self):
        data = dict(lookup="19.117.63.126")
        user = UserFactory()
        request = HttpRequest()
        request.user = user
        serializer = GeolocationRequestSerializer(data=data, context=dict(request=request))

        serializer.is_valid(raise_exception=True)
        request = serializer.save()

        self.assertEqual(request.user, user)
        self.assertEqual(request.lookup, data['lookup'])
        self.assertEqual(request.created_at, timezone.now())

        geolocation = request.geolocation

        self.assertEqual(geolocation.ip, '185.157.15.59')
        self.assertEqual(geolocation.type, 'ipv4')
        self.assertEqual(geolocation.continent_code, 'EU')
        self.assertEqual(geolocation.continent_name, 'Europe')
        self.assertEqual(geolocation.country_code, 'PL')
        self.assertEqual(geolocation.country_name, 'Poland')
        self.assertEqual(geolocation.region_code, 'MA')
        self.assertEqual(geolocation.region_name, 'MA')
        self.assertEqual(geolocation.city, 'Wieliczka')
        self.assertEqual(geolocation.zip, '32-005')
        self.assertEqual(geolocation.latitude, '49.96186828613281')
        self.assertEqual(geolocation.longitude, '20.173749923706055')
