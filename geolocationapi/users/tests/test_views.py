from django.contrib.auth.models import User
from django.urls import reverse
from djangorestframework_camel_case.util import camelize
from rest_framework.test import APITestCase
from users.serializers import SignupSerializer


class SignUpUserViewTest(APITestCase):
    def test_sign_up(self):
        data = {
            "username": "demo",
            "first_name": "John",
            "last_name": "Snow",
            "email": "john.snow@example.com",
            "password": "8X@y5e@ec!rQ^XE0",  # nosec
        }

        response = self.client.post(reverse('users:sign-up'), data=data)
        self.assertEqual(response.status_code, 201)
        user = User.objects.get()
        self.assertEqual(response.json(), camelize(SignupSerializer(user).data))
