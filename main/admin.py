from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from . import models


class ServiceInline(admin.TabularInline):
    model = models.Service
    extra = 0
    show_change_link = True


class RequestInline(admin.TabularInline):
    model = models.Request.companies.through
    extra = 0
    show_change_link = True
    verbose_name = _("request")
    verbose_name_plural = _("requests")


class NotificationInline(admin.TabularInline):
    model = models.Notification
    extra = 0
    show_change_link = True


@admin.register(models.Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ("owner", "name")
    date_hierarchy = "created_at"
    inlines = (ServiceInline, RequestInline, NotificationInline)
    search_fields = ("name", "owner__email")


@admin.register(models.Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ("id", "company", "get_customer", "status")
    list_filter = ("status",)
    date_hierarchy = "created_at"
    search_fields = ("company__name", "request__customer__email")

    @admin.display(description="customer")
    def get_customer(self, obj):
        return obj.request.customer


@admin.register(models.Rating)
class RatingAdmin(admin.ModelAdmin):
    list_display = ("company", "customer", "rating")
    list_filter = ("rating",)
    search_fields = ("company__name", "customer__name")
    date_hierarchy = "created_at"


@admin.register(models.Request)
class RequestAdmin(admin.ModelAdmin):
    list_display = ("customer", "status")
    list_filter = ("status",)
    filter_horizontal = ("companies",)
    date_hierarchy = "created_at"


@admin.register(models.Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ("company", "name", "price")
    list_filter = ("company",)
    search_fields = ("company__name", "name")
    date_hierarchy = "created_at"
