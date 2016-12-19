import random
import string
from uuid import uuid4
from django.conf import settings
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser


class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **other_fields):
        if not email:
            raise ValueError(_('Users must have an email address'))

        user = self.model(email=self.normalize_email(email), **other_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        return self.create_user(
            email=email,
            password=password,
            is_staff=True,
            is_superuser=True,
            email_confirmed=True,
        )


class CustomUser(AbstractBaseUser):
    email = models.EmailField(max_length=256, unique=True, db_index=True, verbose_name=_('E-mail'))
    user_name = models.CharField(max_length=30, blank=True, verbose_name=_('User name'))

    #####
    about = models.TextField(blank=True, null=True, verbose_name='About')
    website = models.URLField(blank=True, null=True, verbose_name='Website')
    twitter = models.URLField(blank=True, null=True, verbose_name='Twitter')
    facebook = models.URLField(blank=True, null=True, verbose_name='Facebook')
    instagram = models.URLField(blank=True, null=True, verbose_name='Instagram')
    pinterest = models.URLField(blank=True, null=True, verbose_name='Pinterest')
    #####

    is_active = models.BooleanField(default=True, verbose_name=_('Is active'))
    is_staff = models.BooleanField(default=False, verbose_name=_('Is staff'))
    is_superuser = models.BooleanField(default=False, verbose_name=_('Is superuser'))

    email_confirmed = models.BooleanField(default=False, verbose_name=_('Email confirmed'))

    date_joined = models.DateTimeField(auto_now_add=True, verbose_name=_('Date joined'))

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def get_full_name(self):
        return self.email

    def get_short_name(self):
        return self.user_name

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True


REASON_CONFIRM = 0
REASON_RESET = 1
REASON_CHOICES = (
    (REASON_CONFIRM, _('E-mail confirm')),
    (REASON_RESET, _('Password reset')),
)


def random_word(length=24):
        return ''.join(random.choice(string.ascii_letters) for i in range(length))


def generate_token():
    return str(uuid4().int)


class UserConfirmToken(models.Model):
    user = models.ForeignKey(CustomUser, related_name='user_tokens', verbose_name=_('Token owner'))
    uid = models.CharField(max_length=24, default=random_word, verbose_name=_('Token uid'))
    token = models.CharField(max_length=50, default=generate_token, verbose_name=_('Token'))
    reason = models.PositiveSmallIntegerField(choices=REASON_CHOICES, verbose_name=_('Reason'))
    used = models.BooleanField(default=False, verbose_name=_('Used'))
    created = models.DateTimeField(auto_now_add=True, verbose_name=_('Created'))

    def __str__(self):
        return 'User_{} token'.format(self.user.pk)
