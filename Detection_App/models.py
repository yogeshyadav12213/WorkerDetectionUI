# In Detection_App/models.py

from django.db import models

class Camera(models.Model):
    STATUS_CHOICES = [
        ('online', 'Online'),
        ('offline', 'Offline'),
    ]

    camera_id = models.CharField(max_length=50, unique=True, help_text="e.g., CAM-001")
    name = models.CharField(max_length=100, default="Unnamed Camera")
    ip_address = models.GenericIPAddressField(unique=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='offline')
    resolution = models.CharField(max_length=20, blank=True, null=True, help_text="e.g., 1920x1080")
    fps = models.PositiveIntegerField(default=30)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} ({self.ip_address})"

    class Meta:
        ordering = ['created_at']

class Zone(models.Model):
    camera = models.ForeignKey(Camera, on_delete=models.CASCADE, related_name='zones')
    name = models.CharField(max_length=100)
    coordinates = models.JSONField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Zone '{self.name}' on {self.camera.name}"