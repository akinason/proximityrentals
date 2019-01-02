from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone

from main.models import User, UserManager


class App(models.Model):
    name = models.CharField(_('application name'), max_length=100)
    key = models.CharField(_('application key'), max_length=100, blank=True)
    secret = models.CharField(_('application secret'), max_length=100, blank=True)
    is_active = models.BooleanField(default=True)
    user = models.ForeignKey(User, related_name='apps', on_delete=models.CASCADE, blank=True, null=True)
    is_deleted = models.BooleanField(default=False)
    created_on = models.DateTimeField(default=timezone.now)
    deleted_on = models.DateTimeField(blank=True, null=True)
    is_admin = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    def set_keys(self):
        user_manager = UserManager()
        while True:
            key = user_manager.make_random_password(length=50)
            if not App.objects.filter(key=key).exists():
                self.key = key
                break 
        
        while True:
            secret = user_manager.make_random_password(length=50)
            if not App.objects.filter(secret=secret).exists():
                self.secret = secret
                break 
        return True

