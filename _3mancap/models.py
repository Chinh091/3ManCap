from django.db import models

# Create your models here.
# _3mancap/models.py

from django.db import models

class ActivityLog(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    description = models.CharField(max_length=255)

class Device(models.Model):
    name = models.CharField(max_length=100)
    connected = models.BooleanField(default=False)

class Incident(models.Model):
    description = models.TextField()
    resolved = models.BooleanField(default=False)

class Event(models.Model):
    name = models.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now_add=True)
