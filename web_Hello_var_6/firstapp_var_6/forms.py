from django import forms

class ProductForm(forms.Form):
    name = forms.CharField(
        label='Название товара',
        widget=forms.TextInput(attrs={'placeholder': 'Введите название товара'})
    )
    price = forms.DecimalField(
        label='Цена',
        max_digits=10,
        decimal_places=2,
        min_value=0.01,
        widget=forms.NumberInput(attrs={'step': '0.01', 'placeholder': '0.00'})
    )
    quantity = forms.IntegerField(
        label='Количество',
        min_value=1,
        widget=forms.NumberInput(attrs={'placeholder': '1'})
    )
    category = forms.CharField(  # ИЗМЕНИЛИ НА CharField
        label='Категория',
        max_length=100,
        widget=forms.TextInput(attrs={'placeholder': 'Введите категорию товара'})
    )

class MovementForm(forms.Form):
    product = forms.ChoiceField(
        label='Выберите товар',
        choices=[],
        widget=forms.Select
    )
    stores = forms.ChoiceField(  # ОСТАВЛЯЕМ ChoiceField
        label='Выберите магазин',  # Изменили на единственное число
        choices=[],
        widget=forms.RadioSelect  # ОСТАВЛЯЕМ RadioSelect
    )
    quantity = forms.IntegerField(
        label='Количество для перемещения',
        min_value=1,
        initial=1
    )
    worker = forms.ChoiceField(
        label='Кладовщик',
        choices=[],
        widget=forms.RadioSelect
    )
    date = forms.DateField(
        label='Дата перемещения',
        widget=forms.DateInput(attrs={'type': 'date'})
    )