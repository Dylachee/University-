from rest_framework.permissions import SAFE_METHODS, BasePermission


class IsAuthorOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, user):
        return bool(
            request.method in SAFE_METHODS or
            (request.user and request.user.is_authenticated and
             user == request.user)
        )