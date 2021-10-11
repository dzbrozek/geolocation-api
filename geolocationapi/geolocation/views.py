from typing import cast

from django.contrib.auth.models import User
from django.db import models
from geolocation.models import GeolocationRequest
from geolocation.serializers import GeolocationRequestSerializer
from rest_framework import mixins
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import GenericViewSet


class GeolocationRequestViewSet(
    mixins.CreateModelMixin, mixins.RetrieveModelMixin, mixins.DestroyModelMixin, mixins.ListModelMixin, GenericViewSet
):
    serializer_class = GeolocationRequestSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self) -> models.QuerySet["GeolocationRequest"]:
        return GeolocationRequest.objects.filter(user=cast(User, self.request.user)).select_related('geolocation')
