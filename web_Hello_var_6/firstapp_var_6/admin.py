from django.contrib import admin
from .models import Product, Movement#, ProductCategory, , Category

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price']
    list_filter = ['category']
    search_fields = ['name']

@admin.register(Movement)
class MovementAdmin(admin.ModelAdmin):
    list_display = ['product', 'store', 'quantity', 'date']
    list_filter = ['date', 'store']


# @admin.register(Category)
# class CategoryAdmin(admin.ModelAdmin):
#     list_display = ['name']  # Убрали 'description'
#     search_fields = ['name']
#
#
#
# @admin.register(ProductCategory)
# class ProductCategoryAdmin(admin.ModelAdmin):
#     list_display = ['product', 'category', 'assigned_at']
#     list_filter = ['category']
#
