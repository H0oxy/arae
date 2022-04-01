from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.db import models


class KpkUserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, login, email, password, **extra_fields):
        """
        Create and save a user with the given login, email, and password.
        """
        if not login:
            raise ValueError('The given login must be set')
        email = self.normalize_email(email)
        user = self.model(login=login, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, login, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(login, email, password, **extra_fields)

    def create_superuser(self, login, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(login, email, password, **extra_fields)


class KpkUser(AbstractUser):
    objects = KpkUserManager()

    username = None
    first_name = None
    last_name = None

    login = models.CharField(
        'username',
        max_length=150,
        unique=True,
        help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.',
        validators=[AbstractUser.username_validator],
        error_messages={
            'unique': "A user with that username already exists.",
        },
    )
    USERNAME_FIELD = 'login'

    name = models.CharField('name', max_length=150, )
    surname = models.CharField('surname', max_length=150)
    email = models.EmailField('email address')
    patronymic = models.CharField('patronymic', max_length=150, blank=True)
    rules = models.BooleanField('rules', default=True)

    def get_full_name(self):
        """
        Return the first_name plus the last_name, with a space in between.
        """
        full_name = '%s %s' % (self.name, self.surname)
        return full_name.strip()
