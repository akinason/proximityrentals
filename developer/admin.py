from django.contrib import admin
from developer import models


class DeveloperAdmin(admin.ModelAdmin):
    pass 

admin.site.register(models.App, DeveloperAdmin)