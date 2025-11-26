from django import forms
from .models import Product, Movement #, Category, , ProductCategory

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price', 'category', 'photo']

class MovementForm(forms.ModelForm):
    class Meta:
        model = Movement
        fields = ['product', 'store', 'quantity', 'date']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
        }
        labels = {
            'product': 'Товар',
            'store': 'Магазин',
            'quantity': 'Количество',
            'date': 'Дата перемещения',
        }

#
# class CategoryForm(forms.ModelForm):
#     class Meta:
#         model = Category
#         fields = ['name']
