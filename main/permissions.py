from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    custom permission to only allow owners of an object to edit it
     """

    def has_object_permission(self, request, view, obj):
        # Read permission are allowed on any requests
        # so we'll always allow GET, HEAD, or OPTIONS request.

        if request.method in permissions.SAFE_METHODS:
            return True

        # Write permissions are only allowed to owners
        return obj.user == request.user


class IsUserOrReadOnly(permissions.BasePermission):
    """
    Permission class for user account editing and deletion. The default IsOwnerOrReadOnly does not work
    as User model has no obj.user

    Here we check against the obj.pk rather than obj.user
    """
    def has_object_permission(self, request, view, obj):
        # Read permission are allowed on any requests
        # so we'll always allow GET, HEAD, or OPTIONS request.

        if request.method in permissions.SAFE_METHODS:
            return True

        # Write permissions are only allowed to the same users.

        return obj.pk == request.user.pk
