from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

NULLABLE = {'blank': True, 'null': True}


class UserRoles(models.TextChoices):
    MEMBER = 'member', _('member')
    MODERATOR = 'moderator', _('moderator')


class User(AbstractUser):
    username = models.CharField(max_length=35, verbose_name='Username', **NULLABLE)

    email = models.EmailField(unique=True, verbose_name='E-Mail')
    age = models.PositiveIntegerField(**NULLABLE)

    phone = models.CharField(max_length=35, verbose_name='Phone', **NULLABLE)
    telegram = models.CharField(max_length=150, verbose_name='Telegram Username', **NULLABLE)
    avatar = models.ImageField(upload_to='users/', verbose_name='Avatar', **NULLABLE)

    role = models.CharField(max_length=9, choices=UserRoles.choices, default=UserRoles.MEMBER)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return f'{self.username} ({self.telegram})'

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'