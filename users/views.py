from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework import permissions
from users.serializers import UserSerializer

class UserRegistryView(APIView):
    """
    User registry.  Input example:
    {
        "username":"myusername"
        "email": "myemail@email.com",
        "password": "mysuperpassword",
    }
    """
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        try:
            serializer =  UserSerializer(data = request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
