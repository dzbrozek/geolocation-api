import factory.fuzzy
from django.contrib.auth.models import User
from geolocations.models import Geolocation, GeolocationRequest

USER_PASSWORD = 'password'  # nosec


class UserFactory(factory.django.DjangoModelFactory):
    username = factory.Sequence(lambda n: f'user-{n}')
    email = factory.Sequence(lambda n: f'user-{n}@example.com')
    password = factory.PostGenerationMethodCall('set_password', USER_PASSWORD)
    is_active = factory.Faker('pybool')

    class Meta:
        model = User
        django_get_or_create = ('username',)


class GeolocationFactory(factory.django.DjangoModelFactory):
    request = factory.SubFactory('geolocation.factories.GeolocationRequestFactory')
    ip = factory.Faker('ipv4')
    type = factory.fuzzy.FuzzyChoice(choices=["ipv4", "ipv6"])
    continent_code = factory.fuzzy.FuzzyText(length=2)
    continent_name = factory.fuzzy.FuzzyText(length=10)
    country_code = factory.Faker('country_code')
    country_name = factory.Faker('country')
    region_code = factory.fuzzy.FuzzyText(length=2)
    region_name = factory.fuzzy.FuzzyText(length=10)
    city = factory.Faker('city')
    zip = factory.Faker('postcode')
    latitude = factory.Faker('latitude')
    longitude = factory.Faker('longitude')

    class Meta:
        model = Geolocation


class GeolocationRequestFactory(factory.django.DjangoModelFactory):
    lookup = factory.Faker('ipv4')
    user = factory.SubFactory(UserFactory)
    geolocation = factory.RelatedFactory(
        GeolocationFactory,
        factory_related_name='request',
    )

    class Meta:
        model = GeolocationRequest
