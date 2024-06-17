from django.conf import settings
from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed

__all__ = ["APIKeyAuthentication"]


class APIKeyAuthentication(BaseAuthentication):
    def authenticate(self, request):
        api_key = request.headers.get("Authorization")
        if not api_key or api_key != settings.API_KEY:
            raise AuthenticationFailed("Invalid or missing API key")
        return None, None
