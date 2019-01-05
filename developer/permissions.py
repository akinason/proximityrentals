from rest_framework import permissions
from developer.models import App

"""
This file stores mostly API permissions. 
"""


class HasAPIAccess(permissions.BasePermission):
    #  Returns True if the API_KEY is provided in the request and 
    message = 'Invalid or missing API Key.'

    def has_permission(self, request, view):
        api_key = request.META.get('HTTP_API_KEY', '')
        if api_key:
            return App.objects.filter(key=api_key, is_active=True).exists()
        return False

class HasAPISuperAccess(permissions.BasePermission):
    # This is the permission needed for an API to use the endpoints neccessary for creating applications.
    message = 'Invalid, missing or unauthorized API Key.'
    
    def has_permission(self, request, view):
        api_key = request.META.get('HTTP_API_KEY', '')
        if api_key:
            return App.objects.filter(key=api_key, is_active=True, is_admin=True).exists()
        return False
    


class HasAPIWritePermissionOrReadOnly(permissions.BasePermission):
    # Ensure only some API keys can create, update and delete objects. Read permission allowed for everyone.

    message = 'API Key does not allow PUT, DELETE and POST requests.'

    def has_permission(self, request, view):
        api_key = request.META.get('HTTP_API_KEY', '')

        if api_key:
            if request.method in permissions.SAFE_METHODS:  # Simply check if the API key exists and is active.
                return App.objects.filter(key=api_key, is_active=True).exists()
            else:  # Check if the API key has write permissions.
                return App.objects.filter(key=api_key, is_active=True, write=True).exists()
        return False