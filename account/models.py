from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create(self, email, password, **k):
        if not email:
            raise ValueError('email is required')
        email = self.normalize_email(email)
        # self.model = User 
        user = self.model(email=email, **k)
        user.set_password(password) #heshiruet i ustanavlivaet parol
        user.save(using=self._db) #sohranyaet v db
        return user


    def create_user(self, email, password, **k):
        return self._create(email, password, **k)


    def create_superuser(self,  email, password, **k ):
        k.setdefault('is_staff', True)
        k.setdefault('is_superuser', True)
        k.setdefault('is_active', True)
      
        return self._create(email, password, **k)


class User(AbstractUser):
    email = models.EmailField(unique=True)
    # password =models.CharField(max_length=20) delete 0001_initial_
    username = None

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()







































