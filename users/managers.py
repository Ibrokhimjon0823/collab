from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model
from django.db.models import manager


class CustomUserManager(BaseUserManager):
    use_in_migrations = True

    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError(_("Email must be set"))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(self._db)
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_("Superuser must have is_staff=True."))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_("Superuser must have is_superuser=True."))
        return self.create_user(email, password, **extra_fields)


class CompanyUserManager(manager.Manager):
    def get_queryset(self):
        return (
            super(CompanyUserManager, self)
                .get_queryset()
                .filter(role=get_user_model().Role.COMPANY)
        )


class CustomerUserManager(manager.Manager):
    def get_queryset(self):
        return (
            super(CustomerUserManager, self)
                .get_queryset()
                .filter(role=get_user_model().Role.CUSTOMER)
        )

