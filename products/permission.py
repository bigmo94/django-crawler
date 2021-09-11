from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsUserAdminOrViewer(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        elif request.user.is_superuser:
            return True
        return False
