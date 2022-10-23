from rest_framework import permissions

"""custom permissions"""


class ContributorReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return bool(request.user)


class AuthorAccess(permissions.BasePermission):
    def has_permission(self, request, view):
        return True