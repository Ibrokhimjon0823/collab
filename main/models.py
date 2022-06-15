from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils.translation import gettext_lazy as _

from core.models import BaseModel


class Company(BaseModel):
    owner = models.OneToOneField(
        "users.CustomUser",
        on_delete=models.CASCADE,
        verbose_name=_("Owner")
    )
    name = models.CharField(_("Name"), max_length=60)

    class Meta:
        verbose_name = _("Company")
        verbose_name_plural = _("Companies")

    def __str__(self):
        return self.name


class Service(BaseModel):
    company = models.ForeignKey(
        Company,
        on_delete=models.CASCADE,
        related_name="services",
        related_query_name="service",
        verbose_name=_("Company")
    )
    name = models.CharField(_("Name"), max_length=60)
    price = models.DecimalField(_("Price"), max_digits=8, decimal_places=2)

    class Meta:
        verbose_name = _("Service")
        verbose_name_plural = _("Services")

    def __str__(self):
        return self.name


class Rating(BaseModel):
    company = models.ForeignKey(
        Company,
        on_delete=models.CASCADE,
        related_name="ratings",
        related_query_name="rating",
        verbose_name=_("Company")
    )
    customer = models.ForeignKey(
        "users.CustomerUser",
        on_delete=models.CASCADE,
        related_name="ratings",
        related_query_name="rating",
        verbose_name=_("Customer"),
        null=True
    )
    rating = models.PositiveIntegerField(_("Rating"), validators=[MaxValueValidator(5)])
    comment = models.TextField(_("Comment"), blank=True, null=True)

    class Meta:
        verbose_name = _("Rating")
        verbose_name_plural = _("Ratings")

    def __str__(self):
        return f"{self.company.__str__()} - {self.rating}"


class Request(BaseModel):
    class Status(models.TextChoices):
        PENDING = "pending", _("Pending")
        APPROVED = "approved", _("Approved")
        REJECTED = "rejected", _("Rejected")

    customer = models.ForeignKey(
        "users.CustomUser",
        on_delete=models.CASCADE,
        related_name="requests",
        related_query_name="request",
        limit_choices_to={"role": "customer"},
        verbose_name=_("Customer")
    )
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name='requests')
    country = models.CharField(_("Country"), max_length=60)
    city = models.CharField(_("City"), max_length=60)
    street = models.CharField(_("Street"), max_length=60)
    house_number = models.CharField(_("House Number"), max_length=60)
    apartment = models.CharField(_("Apartment"), max_length=60, blank=True)
    status = models.CharField(_("Status"), max_length=20, choices=Status.choices, default=Status.PENDING)
    duration = models.DecimalField(
        _("Duration"),
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(0)],
    )
    area = models.DecimalField(
        _("Area"), max_digits=10, decimal_places=2, validators=[MinValueValidator(0)]
    )

    @property
    def total_cost(self):
        return self.service.price * self.duration

    class Meta:
        verbose_name = _("Request")
        verbose_name_plural = _("Requests")

    def __str__(self):
        return f"{self.customer.__str__()} - {self.status}"


class Notification(BaseModel):
    class Status(models.TextChoices):
        SEEN = "seen", _("Seen")
        UNSEEN = "unseen", _("Unseen")

    company = models.ForeignKey(
        Company,
        on_delete=models.CASCADE,
        related_name="notifications",
        related_query_name="notification",
        verbose_name=_("Company")
    )
    request = models.ForeignKey(Request, on_delete=models.CASCADE, verbose_name=_("request"))
    status = models.CharField(_("Status"), max_length=20, choices=Status.choices, default=Status.UNSEEN)

    class Meta:
        verbose_name = _("Notification")
        verbose_name_plural = _("Notifications")

    def __str__(self):
        return f"{self.company.__str__()} - {self.status}"

