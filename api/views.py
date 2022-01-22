# from django.shortcuts import render
# from django.contrib.auth.models import User
# from rest_framework.response import Response
# from rest_framework.views import APIView
# from rest_framework.decorators import api_view
# from rest_framework import status
# from api.serializers import UserSerializer

# class UserRegisterView(APIView):
#     def post(self, request):
#         try:
#             serializer =  UserSerializer(data = request.data)
#             serializer.is_valid(raise_exception=True)
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         except:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)