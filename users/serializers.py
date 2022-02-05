from django.contrib import auth
from rest_framework import serializers
from rest_framework import exceptions
from users.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        # fields = [
        #     'id',
        #     'username',
        #     'email',
        #     'password',
        # ]
        fields = '__all__'
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        user = User.objects.create(**validated_data)
        password = user.password
        user.set_password(password)
        user.save()
        return user

class LoginSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=100)
    email = serializers.EmailField(max_length=100)
    password = serializers.CharField(max_length=100, write_only=True)
    tokens = serializers.CharField(max_length=100, read_only=True)

    class Meta:
        model = User
        #fields = '__all__'
        fields = [
            'username',
            'email',
            'password',
            'tokens',
        ]

    def validate(self, attrs):
        username = attrs.get('username','')
        email = attrs.get('email','')
        password = attrs.get('password','')

        user = auth.authenticate(username=username, email=email, password=password)

        if not user:
            raise exceptions.AuthenticationFailed('Invalid credentials. Try again.')

        if not user.is_active:
            raise exceptions.AuthenticationFailed('Account inactive.')

        if not user.is_verified:
            raise exceptions.AuthenticationFailed('Account not verified.')

        return {
            'username': user.username,
            'email': user.email,
            'tokens': user.tokens
        }

        #return super().validate(attrs)

# class UserSerializer(serializers.Serializer):
#     id = serializers.ReadOnlyField()
#     username = serializers.CharField()
#     email = serializers.EmailField()
#     password = serializers.CharField()
#     # first_name = serializers.CharField()
#     # last_name = serializers.CharField()

#     def create(self, validated_data):
#         instance = User()
#         instance.username = validated_data.get('username')
#         instance.email = validated_data.get('email')
#         instance.password(validated_data.get('password'))
#         instance.save()
#         return instance

#     def validate_username(self, data):
#         users = User.objects.filter(username = data)
        
#         if len(users) != 0:
#             raise serializers.ValidationError('Username already exists, choose a new one.')
#         else:
#             return data
