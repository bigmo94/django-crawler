from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsUserOwnerOrJustRead(BasePermission):
    # def has_permission(self, request, view):
    #     if request.method in SAFE_METHODS:
    #         return True
    #     return False

    def has_object_permission(self, request, view, obj):
        if obj.profile.user != request.user:
            return False
        return True


class IsUserAdmin(BasePermission):
    def has_object_permission(self, request, view, obj):
        if obj.profile.user != request.user:
            return False
        if not obj.profile.user.is_admin:
            return False
        return True
