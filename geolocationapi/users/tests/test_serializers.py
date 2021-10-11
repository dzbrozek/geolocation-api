from django.test import TestCase
from geolocations.factories import UserFactory
from rest_framework.exceptions import ErrorDetail
from users.serializers import SignupSerializer


class SignupSerializerTest(TestCase):
    def test_empty_data(self):
        data = dict()
        serializer = SignupSerializer(data=data)

        self.assertFalse(serializer.is_valid())
        self.assertEqual(
            serializer.errors,
            {
                'username': [ErrorDetail(string='This field is required.', code='required')],
                'first_name': [ErrorDetail(string='This field is required.', code='required')],
                'last_name': [ErrorDetail(string='This field is required.', code='required')],
                'email': [ErrorDetail(string='This field is required.', code='required')],
                'password': [ErrorDetail(string='This field is required.', code='required')],
            },
        )

    def test_duplicate_username(self):
        UserFactory(username="demo", email="john.snow@example.com")
        data = dict(  # nosec
            username="demo",
            first_name="John",
            last_name="Snow",
            email="john.snow@example.com",
            password="8X@y5e@ec!rQ^XE0",
        )
        serializer = SignupSerializer(data=data)

        self.assertFalse(serializer.is_valid())
        self.assertEqual(
            serializer.errors,
            {
                'username': [ErrorDetail(string='A user with that username already exists.', code='unique')],
            },
        )

    def test_common_password(self):
        data = dict(  # nosec
            username="demo",
            first_name="John",
            last_name="Snow",
            email="john.snow@example.com",
            password="password",
        )
        serializer = SignupSerializer(data=data)

        self.assertFalse(serializer.is_valid())
        self.assertEqual(
            serializer.errors,
            {'password': [ErrorDetail(string='This password is too common.', code='password_too_common')]},
        )

    def test_create_user(self):
        data = dict(  # nosec
            username="demo",
            first_name="John",
            last_name="Snow",
            email="john.snow@example.com",
            password="8X@y5e@ec!rQ^XE0",
        )
        serializer = SignupSerializer(data=data)

        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        self.assertEqual(user.username, data['username'])
        self.assertEqual(user.first_name, data['first_name'])
        self.assertEqual(user.last_name, data['last_name'])
        self.assertEqual(user.email, data['email'])
        self.assertTrue(user.check_password(data['password']))
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_superuser)
        self.assertFalse(user.is_staff)
