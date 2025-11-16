from django import forms
from .models import Product, Movement

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price', 'category', 'photo']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Название товара'}),
            'price': forms.NumberInput(attrs={'step': '0.01', 'placeholder': '0.00'}),
            'category': forms.TextInput(attrs={'placeholder': 'Категория товара'}),
            'photo': forms.FileInput(attrs={'accept': 'image/*'}),
        }
        labels = {
            'name': 'Название товара',
            'price': 'Цена (руб.)',
            'category': 'Категория',
            'photo': 'Фото товара',
        }

class MovementForm(forms.ModelForm):
    class Meta:
        model = Movement
        fields = ['product', 'store', 'quantity', 'date', 'worker']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'store': forms.TextInput(attrs={'placeholder': 'Название магазина'}),
            'worker': forms.TextInput(attrs={'placeholder': 'ФИО кладовщика'}),
        }
        labels = {
            'product': 'Товар',
            'store': 'Магазин',
            'quantity': 'Количество',
            'date': 'Дата перемещения',
            'worker': 'Кладовщик',
        }