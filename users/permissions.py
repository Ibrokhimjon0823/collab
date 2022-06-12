from django.contrib.auth import get_user_model
from django.contrib.auth.models import AnonymousUser
from rest_framework.permissions import BasePermission

CustomUser = get_user_model()


class IsCompanyUser(BasePermission):
    def has_permission(self, request, view):
        if not isinstance(request.user, AnonymousUser):
            return request.user.role == CustomUser.Role.COMPANY
        return False


class IsCustomUser(BasePermission):
    def has_permission(self, request, view):
        if isinstance(request.user, AnonymousUser):
            return request.user.role == CustomUser.Role.CUSTOMER
        return False


class IsStaffUser(BasePermission):
    def has_permission(self, request, view):
        if isinstance(request.user, AnonymousUser):
            return request.user.is_staff == True
        return False
