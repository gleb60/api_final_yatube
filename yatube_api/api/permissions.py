from rest_framework import permissions


class IsAuthorOrReadOnly(permissions.BasePermission):
    """
    Read : anyone
    Delete : admin only
    Create, Update : author only
    """

    def has_object_permission(self, request, view, obj):
        # Anyone can read (HTTP method : GET, HEAD, and OPTIONS)
        if request.method in permissions.SAFE_METHODS:
            return True
        # Only author can create and update (HTTP method : POST, PUT, PATCH)
        return obj.author == request.user
