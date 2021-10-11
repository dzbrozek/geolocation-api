from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny

from .serializers import SignupSerializer


@extend_schema_view(
    post=extend_schema(description='Creates a new user account'),
)
class SignUpUserView(CreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = SignupSerializer
