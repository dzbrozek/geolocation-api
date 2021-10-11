import logging
from urllib.parse import urlsplit

import requests.exceptions
from django.core.exceptions import ValidationError as DjangoValidationError
from django.core.validators import URLValidator, validate_ipv46_address
from django.db import transaction
from geolocations.clients import get_ipstack_client
from geolocations.clients.ipstack import IPStackException
from geolocations.models import Geolocation, GeolocationRequest
from rest_framework import serializers

logger = logging.getLogger(__name__)


class GeolocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Geolocation
        fields = (
            "ip",
            "type",
            "continent_code",
            "continent_name",
            "country_code",
            "country_name",
            "region_code",
            "region_name",
            "city",
            "zip",
            "latitude",
            "longitude",
        )


class GeolocationRequestSerializer(serializers.ModelSerializer):
    geolocation = GeolocationSerializer(read_only=True)

    class Meta:
        model = GeolocationRequest
        fields = ("id", "lookup", "created_at", "geolocation")
        read_only_fields = ['created_at']

    def validate_lookup(self, value: str) -> str:
        try:
            validate_ipv46_address(value)
            return value
        except DjangoValidationError:
            try:
                if '://' not in value:
                    value = f'https://{value}'
                URLValidator()(value)
                return urlsplit(value)[1]
            except DjangoValidationError:
                pass

        raise serializers.ValidationError("Provide a valid IP address or URL")

    @transaction.atomic
    def create(self, validated_data: dict) -> GeolocationRequest:
        lookup = validated_data['lookup']
        ipstack_client = get_ipstack_client()

        try:
            response = ipstack_client.lookup(lookup)
        except IPStackException as e:
            logger.exception("Unable to look up address: %s", e)
            raise serializers.ValidationError(str(e))
        except requests.exceptions.RequestException as e:
            logger.exception("Unable to look up address: %s", e)
            raise serializers.ValidationError("Unable to look up given address")

        request = GeolocationRequest.objects.create(user=self.context['request'].user, lookup=lookup)
        Geolocation.objects.create(
            request=request,
            ip=response['ip'],
            type=response['type'],
            continent_code=response['continent_code'] or '',
            continent_name=response['continent_name'] or '',
            country_code=response['country_code'] or '',
            country_name=response['country_name'] or '',
            region_code=response['region_code'] or '',
            region_name=response['region_name'] or '',
            city=response['city'] or '',
            zip=response['zip'] or '',
            latitude=str(response['latitude']) if response['latitude'] is not None else None,
            longitude=str(response['longitude']) if response['longitude'] is not None else None,
        )
        return request
