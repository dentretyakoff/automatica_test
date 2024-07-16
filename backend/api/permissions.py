from rest_framework.permissions import BasePermission


class PhoneIsAuthenticated(BasePermission):
    """Авторизация по номеру телефона."""

    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return True
        return False

    def has_object_permission(self, request, view, obj):
        if request.user.is_authenticated:
            return True
        return False
