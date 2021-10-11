from typing import cast

from django.contrib.auth.models import User
from django.db import models
from drf_spectacular.utils import extend_schema, extend_schema_view
from geolocations.models import GeolocationRequest
from geolocations.serializers import GeolocationRequestSerializer
from rest_framework import mixins
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import GenericViewSet


@extend_schema_view(
    list=extend_schema(description='Returns a list of geocoded addresses'),
    create=extend_schema(description='Geocodes given IP or URL address'),
    retrieve=extend_schema(description='Retrieves details of a geocoded address'),
    destroy=extend_schema(description='Destroys a geocoded address'),
)
class GeolocationRequestViewSet(
    mixins.CreateModelMixin, mixins.RetrieveModelMixin, mixins.DestroyModelMixin, mixins.ListModelMixin, GenericViewSet
):
    serializer_class = GeolocationRequestSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self) -> models.QuerySet["GeolocationRequest"]:
        return GeolocationRequest.objects.filter(user=cast(User, self.request.user)).select_related('geolocation')
