from rest_framework import serializers
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
