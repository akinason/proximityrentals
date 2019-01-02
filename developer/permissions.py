from rest_framework import permissions
from developer.models import App


class HasAPIAccess(permissions.BasePermission):
    message = 'Invalid or missing API Key.'

    def has_permission(self, request, view):
        api_key = request.META.get('HTTP_API_KEY', '')
        return App.objects.filter(key=api_key, is_active=True).exists()

class HasAPISuperAccess(permissions.BasePermission):
    # This is the permission needed for an API to use the endpoints neccessary for creating applications.
    message = 'Invalid, missing or unauthorized API Key.'
    
    def has_permission(self, request, view):
        api_key = request.META.get('HTTP_API_KEY', '')
        return App.objects.filter(key=api_key, is_active=True, is_admin=True).exists()