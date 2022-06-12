from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils.translation import gettext_lazy as _

from core.models import BaseModel

from . import managers


class CustomUser(AbstractBaseUser, BaseModel, PermissionsMixin):
    class Role(models.TextChoices):
        COMPANY = "company", _("Company")
        CUSTOMER = "customer", _("Customer")

    name = models.CharField(_("name"), max_length=160)
    email = models.EmailField(_("email address"), unique=True)
    is_staff = models.BooleanField(
        _("staff"),
        default=False,
        help_text=_("Indicates this user is able to log into admin site"),
    )
    is_active = models.BooleanField(
        _("active"),
        default=True,
        help_text=_(
            "Inticates the user is active or not"
        ),
    )
    role = models.CharField(_("Role"), max_length=50, choices=Role.choices)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    objects = managers.CustomUserManager()

    class Meta:
        verbose_name = _("user")
        verbose_name_plural = _("users")

    def __str__(self):
        return self.email


class CompanyUser(CustomUser):
    objects = managers.CompanyUserManager()

    class Meta:
        proxy = True
        verbose_name = _("company user")
        verbose_name_plural = _("company users")


class CustomerUser(CustomUser):
    objects = managers.CustomerUserManager()

    class Meta:
        proxy = True
        verbose_name = _("customer")
        verbose_name_plural = _("customers")

