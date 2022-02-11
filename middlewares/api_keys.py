from django.forms import ValidationError
from app import settings
from rest_framework import exceptions
from rest_framework.response import Response
from rest_framework import status

# Method to check incoming api key clients from frontend.  If exists and it's correct, allow functionality.

def check_api_key_client(self):
    api_key = settings.API_CLIENT

    try:
        front_api_key = self.request.META.get('HTTP_API_KEY', None)
        if front_api_key is None:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        if api_key != front_api_key:
            return Response(status=status.HTTP_403_FORBIDDEN)
        if front_api_key:
            return Response(status=status.HTTP_200_OK)
    except:
        return Response(status=status.HTTP_400_BAD_REQUEST)