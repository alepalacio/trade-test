from django.contrib.auth.base_user import BaseUserManager

class UserManager(BaseUserManager):
    def create_user(self, username, email, password=None):
        if not username:
            raise TypeError("Enter a valid username.")
        if not email:
            raise TypeError("Enter a valid email address.")
        if not password:
            raise TypeError("Enter a valid password.")

        user = self.model(
            email=self.normalize_email(email),
        )
        user.username = username
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username, email, password=None):
        if not username:
            raise TypeError("Enter a valid username.")
        if not email:
            raise TypeError("Enter a valid email address.")
        if not password:
            raise TypeError("Enter a valid password.")

        user = self.model(
            email=self.normalize_email(email),
            is_active=True,
            is_superuser=True,
            is_staff=True,
        )
        user.username = username
        user.set_password(password)
        user.save()
        return user