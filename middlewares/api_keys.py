from app import settings
from rest_framework import exceptions

# Method to check incoming api key clients from frontend.  If exists and it's correct, allow functionality.

def check_api_key_client(self):
    api_key = settings.API_CLIENT
    front_api_key = self.request.META['HTTP_API_KEY']

    if api_key != front_api_key:
        raise exceptions.ValidationError('Missing or invalid API Key')

    return front_api_key