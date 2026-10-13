from django.db import models

# Create your product's models here.

class Warehouse(models.Model):
    name = models.CharField(max_length=60)
    description = models.TextField
    code = models.CharField(max_length=60)
    width = models.IntegerField()
    height = models.IntegerField()
    is_primary = models.BooleanField(default=False, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

class WarehouseSection(models.Model):
    name = models.CharField(max_length=60)
    description = models.TextField
    code = models.CharField(max_length=60)
    width = models.IntegerField()
    height = models.IntegerField()
    is_primary = models.BooleanField(default=False, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    warehouse = models.ForeignKey(Warehouse, related_name="sections", on_delete=models.CASCADE)