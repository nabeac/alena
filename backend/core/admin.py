from django.contrib import admin

from .models.product import Category
# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_active', 'created')
    list_filter = ('created', )
    search_fields = ('title', )