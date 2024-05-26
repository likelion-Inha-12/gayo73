from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from django.utils.crypto import get_random_string

class UserManager(BaseUserManager):
    def create_user(self, email, username, name, password=None):

        user = self.model(
            email=self.normalize_email(email),
            username=username,
            name=name,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, name, password):
        user = self.create_user(
            email,
            username=username,
            name=name,
            password=password,
        )

        user.is_admin = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='email',
        max_length=100,
        unique=True,
    )
    username = models.CharField(max_length=255, unique=True, default="username") #기본 이름 설정
    name = models.CharField(max_length=30)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    generation = models.IntegerField(blank=True, null=True)
    gender = models.CharField(max_length=10, choices=(('male', 'Male'), ('female', 'Female'), ('unknown', 'Unknown')), default='unknown')

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'name']

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin
    
    class Meta:
        db_table = 'user' # 테이블명을 user로 설정
        
# Create your models here.
