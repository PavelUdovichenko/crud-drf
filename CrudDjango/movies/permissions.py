from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    # class gives permissions to change objects to user created this obj
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.user == request.user
