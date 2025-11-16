from django.contrib import admin
from .models import Product, Movement

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'category']
    list_filter = ['category']
    search_fields = ['name']

@admin.register(Movement)
class MovementAdmin(admin.ModelAdmin):
    list_display = ['product', 'store', 'quantity', 'date', 'worker']
    list_filter = ['store', 'date']
    search_fields = ['product__name', 'worker']