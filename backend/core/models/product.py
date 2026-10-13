from django.db import models

from .constants import PRODUCT_STATUS

# Create your product's models here.

class Unit(models.Model):
    name = models.CharField(max_length=60)
    symbol = models.CharField(max_length=20)
    description = models.TextField
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Category(models.Model):
    title = models.CharField(max_length=60)
    description = models.TextField
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    sub_cat = models.ForeignKey("self", on_delete=models.PROTECT, null=True, blank=True)

    def __str__(self):
        return self.title

class Product(models.Model):
    code = models.CharField()
    name = models.CharField(max_length=60)
    description = models.TextField
    barcode = models.CharField(null=True, blank=True)
    min_stock = models.PositiveIntegerField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=1, choices=PRODUCT_STATUS, default='a')
    thumbnail = models.ImageField(upload_to="product/images/", null=True, blank=True)
    attributes = models.JSONField(null=True, blank=True)

    unit = models.ForeignKey(Unit, related_name="products", on_delete=models.PROTECT)
    category = models.ForeignKey(Category, related_name="products", on_delete=models.PROTECT)

    def __str__(self):
        return self.name