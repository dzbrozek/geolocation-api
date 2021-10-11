from django.urls import reverse
from djangorestframework_camel_case.util import camelize
from geolocation.factories import GeolocationRequestFactory, UserFactory
from geolocation.models import GeolocationRequest
from geolocation.serializers import GeolocationRequestSerializer
from rest_framework.test import APITestCase


class GeolocationRequestViewSetListTest(APITestCase):
    def test_cannot_list_as_unauthenticated_user(self):
        response = self.client.get(reverse('geolocation:geolocation-list'))
        self.assertEqual(response.status_code, 401)
        self.assertDictEqual(response.json(), {'detail': 'Authentication credentials were not provided.'})

    def test_list_geolocation_request(self):
        first_user, second_user = UserFactory.create_batch(2, is_active=True)
        first_request = GeolocationRequestFactory(user=first_user)
        GeolocationRequestFactory(user=second_user)

        self.client.force_authenticate(user=first_user)

        response = self.client.get(reverse('geolocation:geolocation-list'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), camelize(GeolocationRequestSerializer([first_request], many=True).data))


class GeolocationRequestViewSetCreateTest(APITestCase):
    def test_cannot_create_as_unauthenticated_user(self):
        data = {'lookup': '155.52.187.7'}
        response = self.client.post(reverse('geolocation:geolocation-list'), data=data)
        self.assertEqual(response.status_code, 401)
        self.assertDictEqual(response.json(), {'detail': 'Authentication credentials were not provided.'})

    def test_create_geolocation_request(self):
        data = {'lookup': '155.52.187.7'}
        user = UserFactory(is_active=True)
        self.client.force_authenticate(user=user)

        response = self.client.post(reverse('geolocation:geolocation-list'), data=data)
        self.assertEqual(response.status_code, 201)
        request = GeolocationRequest.objects.get(user=user)
        self.assertEqual(response.json(), camelize(GeolocationRequestSerializer(request).data))


class GeolocationRequestViewSetDeleteTest(APITestCase):
    def test_cannot_delete_as_unauthenticated_user(self):
        request = GeolocationRequestFactory()
        response = self.client.delete(reverse('geolocation:geolocation-detail', kwargs=dict(pk=request.pk)))

        self.assertEqual(response.status_code, 401)
        self.assertDictEqual(response.json(), {'detail': 'Authentication credentials were not provided.'})

    def test_cannot_delete_someone_else_geolocation_request(self):
        request = GeolocationRequestFactory()
        user = UserFactory(is_active=True)
        self.client.force_authenticate(user=user)

        response = self.client.delete(reverse('geolocation:geolocation-detail', kwargs=dict(pk=request.pk)))

        self.assertEqual(response.status_code, 404)

    def test_delete_geolocation_request(self):
        user = UserFactory(is_active=True)
        request = GeolocationRequestFactory(user=user)
        self.client.force_authenticate(user=user)

        response = self.client.delete(reverse('geolocation:geolocation-detail', kwargs=dict(pk=request.pk)))

        self.assertEqual(response.status_code, 204)
        with self.assertRaises(GeolocationRequest.DoesNotExist):
            request.refresh_from_db()
