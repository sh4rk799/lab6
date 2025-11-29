from django.contrib import admin
from .models import Product, Movement, Category, ProductCategory

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'display_categories']
    list_filter = ['categories']
    search_fields = ['name']

    def display_categories(self, obj):
        return ", ".join([category.name for category in obj.categories.all()])
    display_categories.short_description = 'Категории'

@admin.register(Movement)
class MovementAdmin(admin.ModelAdmin):
    list_display = ['product', 'store', 'quantity', 'date']
    list_filter = ['date', 'store']

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']

@admin.register(ProductCategory)
class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ['product', 'category', 'assigned_at']
    list_filter = ['category', 'assigned_at']