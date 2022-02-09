import jwt
from django.urls import reverse
from django.contrib.sites.shortcuts import get_current_site
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework import permissions
from rest_framework_simplejwt.tokens import RefreshToken
from middlewares.api_keys import check_api_key_client
from users.serializers import UserSerializer, LoginSerializer
from users.models import User
from users.utils import EmailUtil
from app import settings

class UserRegistryView(APIView):
    """
    User registry.  Input example:
    {
        "username":"myusername",
        "email": "myemail@email.com",
        "password": "mysuperpassword"
    }
    """
    permission_classes = [permissions.AllowAny]
        
    def post(self, request):

        try:
            check_api_key_client(self)
            serializer =  UserSerializer(data = request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            user_data = serializer.data
            user = User.objects.get(email=user_data['email'])
            token = RefreshToken.for_user(user).access_token

            current_site = get_current_site(request).domain

            relative_url = reverse('email-verification')

            absolute_url = f"http://{current_site}{relative_url}?t={str(token)}"

            email_body = f"Hi, {user.username}. Please use link below to verify your email account. \n\n{absolute_url}"

            data = {
                'subject':'Verify your email.',
                'body':email_body,
                'to_email':user.email

            }

            EmailUtil.send_email(data)

            return Response('Account successfully created.', status=status.HTTP_201_CREATED)
        except:
            return Response('Bad request.', status=status.HTTP_400_BAD_REQUEST)


class VerifyEmailView(APIView):

    permission_classes = [permissions.AllowAny]

    def get(self, request):

        token = request.GET.get('t')
        
        try:
            payload = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'],)

            user = User.objects.get(id=payload['user_id'])

            if not user.is_verified:
                user.is_verified=True
                user.save()
            return Response('Account succesfully activated.', status=status.HTTP_200_OK)
        except jwt.ExpiredSignatureError as identifier:
            return Response('Activation link expired.', status=status.HTTP_400_BAD_REQUEST)
        except jwt.exceptions.DecodeError as identifier:
            return Response('Invalid token.', status=status.HTTP_400_BAD_REQUEST)


class LiveSearchUsernameAvailabilityView(APIView):
    """
    Retrieves availability information about username input.  Input example:
    {
        "user_input":"myfirstusername"
    }
    """
    permission_classes = [permissions.AllowAny]

    def post(self, request):

        user_input = request.data["user_input"]
        query = User.objects.all().values('username')
        
        for username_data in query:
            username = username_data['username']

            if user_input == username:
                data = {
                    'detail':'Username unavailable. Try again.',
                    'user_input':user_input
                }
                return Response(data, status.HTTP_200_OK)
        
        data = {
            'detail':'Username available.',
            'user_input':user_input
        }
        return Response(data, status=status.HTTP_200_OK)


class UserLoginView(APIView):
    """
    User login.  Input example:
    {
        "username":"myusername",
        "password": "mysuperpassword"
    }
    """
    permission_classes = [permissions.AllowAny]
    
    def post(self, request):
        try:
            check_api_key_client(self)
            serializer = LoginSerializer(data = request.data)
            serializer.is_valid(raise_exception=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except:
            return Response('Bad request.', status=status.HTTP_400_BAD_REQUEST)

class TestView(APIView):
    permissions_classes = permissions.IsAuthenticated

    def get(self, request):
        print(request.user.id)
        return Response('Hola')