from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models


# Create your models here.

class UserManager(BaseUserManager):

    def create_user(self, email, password=None, **extra_kwargs):
        if not email:
            raise ValueError("Enter email")
        user = self.model(email=self.normalize_email(email), **extra_kwargs)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self,email,password=None):
        user = self.create_user(email,password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user





class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=255, unique=True)
    name = models.EmailField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
