# from django.db import models
# from django.contrib.auth.base_user import AbstractBaseUser
# from django.contrib.auth.models import PermissionsMixin
# from api.managers import UserManager

# # Create your models here.

# class User(AbstractBaseUser, PermissionsMixin):
#     username = models.CharField(max_length=100, unique=True)
#     email = models.EmailField(max_length=100, unique=True)
#     password = models.CharField(max_length=100)
#     is_staff = models.BooleanField(default=False)
#     is_active = models.BooleanField(default=True)
#     is_superuser = models.BooleanField(default=False)
#     is_verified = models.BooleanField(default=False)
#     created = models.DateTimeField(auto_now_add=True)
#     updated = models.DateTimeField(auto_now=True)

#     objects = UserManager()

#     USERNAME_FIELD = "username"
#     EMAIL_FIELD = "email"
#     REQUIRED_FIELDS = ['email']

#     def __str__(self):
#         return self.username