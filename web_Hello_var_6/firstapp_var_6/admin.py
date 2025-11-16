from django.contrib import admin
from .models import Category, Product, ProductCategory, Movement

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']  # Убрали 'description'
    search_fields = ['name']

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'category_old']
    list_filter = ['categories']
    search_fields = ['name']

@admin.register(ProductCategory)
class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ['product', 'category', 'assigned_at']
    list_filter = ['category']

@admin.register(Movement)
class MovementAdmin(admin.ModelAdmin):
    list_display = ['product', 'store', 'quantity', 'date']
    list_filter = ['date', 'store']