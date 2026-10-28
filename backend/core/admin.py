from django.contrib import admin

from .models.product import Category, Unit, Product
# Register your models here.

@admin.register(Unit)
class UnitAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_active', 'created')
    list_filter = ('created', )
    search_fields = ('symbol', )


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_active', 'created')
    list_filter = ('created', )
    search_fields = ('title', )


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_active', 'created')
    list_filter = ('created', )
    search_fields = ('name', )

