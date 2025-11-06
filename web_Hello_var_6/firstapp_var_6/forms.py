from django import forms

class ProductForm(forms.Form):
    name = forms.CharField(label='Название товара')
    price = forms.DecimalField(
        label='Цена',
        max_digits=10,  # Максимум 10 цифр всего
        decimal_places=2,  # 2 знака после запятой
        min_value=0.01,  # Минимальная цена
        widget=forms.NumberInput(attrs={'step': '0.01'})  # Шаг 0.01 в браузере
    )
    quantity = forms.IntegerField(label='Количество', min_value=1)
    category = forms.ChoiceField(
        label='Категория',
        choices=[],
        widget=forms.Select
    )

class MovementForm(forms.Form):
    product = forms.ChoiceField(
        label='Выберите товар',
        choices=[],
        widget=forms.Select
    )
    stores = forms.ChoiceField(
        label='Выберите магазины',
        choices=[],
        widget=forms.RadioSelect
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