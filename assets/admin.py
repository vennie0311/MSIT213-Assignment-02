from django.contrib import admin
from .models import Department, User, Asset, MaintenanceLog

admin.site.register(Department)
admin.site.register(User)
admin.site.register(Asset)
admin.site.register(MaintenanceLog)
