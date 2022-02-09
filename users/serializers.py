from django.contrib import auth
from rest_framework import serializers
from rest_framework import exceptions
from users.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        user = User.objects.create(**validated_data)
        password = user.password
        user.set_password(password)
        user.save()
        return user

class LoginSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=100, write_only=True)
    password = serializers.CharField(max_length=100, write_only=True)
    tokens = serializers.CharField(max_length=100, read_only=True)

    class Meta:
        model = User

        fields = [
            'username',
            'password',
            'tokens'
        ]

    def validate(self, attrs):
        username = attrs.get('username')
        password = attrs.get('password')

        if username and password:

            user = auth.authenticate(username=username,password=password)

            if not user:
                msg = 'Unable to log in with provided credentials.'
                raise serializers.ValidationError(msg)

            if not user.is_active:
                msg = 'Account inactive.'
                raise exceptions.ValidationError(msg)

            if not user.is_verified:
                msg = 'Account not verified.'
                raise exceptions.ValidationError(msg)

            tokens = user.tokens

            user_tokens = {
                'tokens':user.tokens
            }

            return user_tokens

        else:
            msg = 'Must include "username" and "password".'
            raise exceptions.ValidationError(msg)