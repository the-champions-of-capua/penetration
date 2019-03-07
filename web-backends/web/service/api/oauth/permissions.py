from rest_framework import permissions

LocalSafeMethod = ["GET", 'POST', 'OPTIONS', 'DELETE', 'PUT']

class OnlyGetAndSupderAdminPermission(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in LocalSafeMethod and request.user.is_superuser():
            return True
        return False


