from django.db import models
from datetime import datetime    
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, User

# Create your models here.
class Neighborhood(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name 

class MyAccountManager(BaseUserManager):
    def create_user(self, email, username, password=None):
        if not email:
            raise ValueError(" User must have an email address")
        if not username:
            raise ValueError(" User must have an username!")    
        
        user = self.model(
            email=self.normalize_email(email),
            username=username,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, username, password):
        user = self.create_user(
            email=self.normalize_email(email),
            password = password,
            username=username,
        )
        user.email = email
        user.is_admin = True 
        user.is_staff = True 
        user.is_superuser = True 
        user.save(using=self._db)
        return user

class Users(AbstractBaseUser):
    username = models.CharField( max_length=20, unique=True)  
    email = models.CharField( max_length=50, unique=True)    
    date_joined = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    last_login = models.DateTimeField(default=timezone.now)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_neighborhood_admin = models.BooleanField(default=False)
    verification_code = models.CharField( max_length=30, null=True)
    name = models.CharField( max_length=60, null=True)
    location = models.CharField(max_length=50, null=True)
    neighborhood_name = models.ForeignKey(Neighborhood, on_delete=models.CASCADE, null=True)
    password = models.CharField( max_length=100)
    
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = [ 'email']
    
    objects=MyAccountManager()
     
    def __str__(self):
        return self.email
    
    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True

        
class Business(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50, null=True)
    user = models.ForeignKey(Users, on_delete=models.CASCADE, null=True)
    neighborhood = models.CharField(max_length=50,null=True)
        

class Heath_center(models.Model):
    name = models.CharField(max_length=50)
    neighborhood =  models.CharField(max_length=50)

class Police_station(models.Model):
    name = models.CharField(max_length=50)
    neighborhood = models.CharField(max_length=50,null=True)

class Emergency_service(models.Model):
    name = models.CharField(max_length=50)
    contact = models.CharField(max_length=50)
    neighborhood = models.CharField(max_length=50,null=True)

class Posts(models.Model):
    title = models.CharField(max_length=50, null=True)
    description = models.CharField(max_length=200)
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.CharField(max_length=50)
    neighborhood = models.CharField(max_length=50,null=True)
