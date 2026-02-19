from django.db import models
from django.contrib.auth.models import AbstractUser

class Department(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class User(AbstractUser):
    department = models.ForeignKey(Department, null=True, blank=True, on_delete=models.SET_NULL, related_name='users')

class Asset(models.Model):
    name = models.CharField(max_length=200)
    cost = models.DecimalField(max_digits=12, decimal_places=2)
    repair_cost = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    assigned_to = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL, related_name='assets')

    def __str__(self):
        return self.name

class MaintenanceLog(models.Model):
    asset = models.ForeignKey(Asset, related_name='maintenance_logs', on_delete=models.CASCADE)
    date = models.DateField()
    description = models.TextField()
    cost = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.asset.name} - {self.date}"
