from django import forms
from .models import Product, Category, Movement, ProductCategory

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price', 'photo']


class MovementForm(forms.ModelForm):
    class Meta:
        model = Movement
        fields = ['product', 'store', 'quantity', 'date']  # Вернули date
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'product': forms.Select(attrs={'class': 'form-control'}),
            'store': forms.TextInput(attrs={'class': 'form-control'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'product': 'Товар',
            'store': 'Магазин',
            'quantity': 'Количество',
            'date': 'Дата перемещения',
        }