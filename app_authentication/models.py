from django.contrib.auth.models import AbstractUser, BaseUserManager, PermissionsMixin
from django.db import models


class AppUserManager(BaseUserManager):

    def create_user(self, email, password, **fields):
        if not email:
            raise ValueError("email is required")
        if not password:
            raise ValueError("email is required")

        user_email = self.normalize_email(email=email)
        user:AppUser = self.model(email=user_email, **fields)
        user.set_password(raw_password=password)
        return user
    

    def create_superuser(self, email, password, **fields,):
        user: AppUser = self.create_user( email=email,password=password, **fields)
        user.is_staff = True
        user.is_superuser =  True
        user.save()
        return user




class AppUser(AbstractUser, PermissionsMixin):
    
    def profile_directory(instance, filename):
        return '/'.join(['images',str(instance.email),filename])

    username = None
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=100, )
    last_name = models.CharField(max_length=100)
    is_staff = models.BooleanField(blank=False, null=False)
    profile_pic = models.ImageField(upload_to=profile_directory, null=True)

    REQUIRED_FIELDS = []
    USERNAME_FIELD = 'email'

    objects = AppUserManager() 

