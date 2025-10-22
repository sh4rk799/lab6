from django import forms

class ProductForm(forms.Form):
    name = forms.CharField(label='Название товара')
    price = forms.IntegerField(label='Цена', min_value=1)
    quantity = forms.IntegerField(label='Количество', min_value=1)
    category = forms.CharField(label='Категория')