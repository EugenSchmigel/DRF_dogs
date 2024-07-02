from rest_framework.permissions import BasePermission

from users.models import UserRoles


class IsModerator(BasePermission):
    message = "You are not the moderator."

    def has_permission(self, request, view):
        if request.user.role == UserRoles.MODERATOR:
            return True
        return False


class IsDogPublic(BasePermission):
    message = "Dog is not published"

    def has_object_permission(self, request, view, obj):
        return obj.is_public


class IsDogOwner(BasePermission):
    message = "You are not the Owner."

    def has_object_permission(self, request, view, obj):
        if request.user == obj.owner:
            return True
        return False
