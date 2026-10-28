from django.db import models

# Create your product's models here.

class Unit(models.Model):
    name = models.CharField(max_length=60, unique=True, error_messages={'unique': "A unit with this title already exists."})
    symbol = models.CharField(max_length=20)
    description = models.TextField(null=True, blank=True)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Category(models.Model):
    title = models.CharField(max_length=60, unique=True, error_messages={'unique': "A category with this title already exists."})
    description = models.TextField(null=True, blank=True)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    sub_cat = models.ForeignKey("self", related_name="children", on_delete=models.PROTECT, null=True, blank=True)

    class Meta:
        verbose_name_plural  = "Categories"

    def __str__(self):
        return self.title

class Product(models.Model):
    code = models.CharField(unique=True, blank=True)
    name = models.CharField(max_length=60, unique=True, error_messages={'unique': "A product with this title already exists."})
    description = models.TextField(null=True, blank=True)
    barcode = models.CharField(null=True, blank=True)
    min_stock = models.PositiveIntegerField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    thumbnail = models.ImageField(upload_to="product/images/", blank=True)
    attributes = models.JSONField(null=True, blank=True)

    unit = models.ForeignKey(Unit, related_name="products", on_delete=models.PROTECT)
    category = models.ForeignKey(Category, related_name="products", on_delete=models.PROTECT)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if not self.code:
            self.code = f"P-{self.pk:06d}"
            super().save(update_fields=["code"])