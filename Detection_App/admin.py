# In Detection_App/admin.py

from django.contrib import admin
from .models import Camera, Zone

@admin.register(Camera)
class CameraAdmin(admin.ModelAdmin):
    list_display = ('name', 'camera_id', 'ip_address', 'status', 'resolution', 'fps')
    list_filter = ('status',)
    search_fields = ('name', 'ip_address', 'camera_id')

@admin.register(Zone)
class ZoneAdmin(admin.ModelAdmin):
    list_display = ('name', 'camera')
    list_filter = ('camera',)
    search_fields = ('name',)