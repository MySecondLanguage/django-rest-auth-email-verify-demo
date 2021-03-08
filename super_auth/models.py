from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models

from random import randint

from django.contrib.postgres.fields import JSONField
from django.utils.translation import ugettext_lazy as _

from super_auth.manager import UserManager

from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
class User(AbstractBaseUser, PermissionsMixin):
    GENDER_CHOICES = (("M", _("Male")), ("F", _("Female")))

    email = models.EmailField(_('email address'), blank=True, unique=True)
    nationality = models.TextField(_("Country"), null=True, blank=True)
    gender = models.CharField(
        _("Gender"), max_length=2, choices=GENDER_CHOICES, null=True, blank=True
    )
    date_of_birth = models.DateField(_("Date of birth"), null=True, blank=True)
    phone_number = models.CharField(_("Phone Number"), null=True, blank=True, max_length=16)
    avatar = models.ImageField(
        _("User Image"), upload_to="avatars/%Y/%m/%d", null=True, blank=True
    )
    is_verified = models.BooleanField(default=False)
    verification_code = models.PositiveIntegerField(
        _("Verification Code"), null=True, blank=True
    )
    full_name = models.CharField(_('First Name'), blank=True, max_length=100)    
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['full_name']
