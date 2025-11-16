from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=200, verbose_name='Название товара')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')
    category = models.CharField(max_length=100, verbose_name='Категория')
    photo = models.ImageField(
        upload_to='products/',
        verbose_name='Фото товара',
        blank=True,
        null=True
    )

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        ordering = ['name']

    def __str__(self):
        return f"{self.name} ({self.price} руб.)"


class Movement(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Товар')
    store = models.CharField(max_length=100, verbose_name='Магазин')
    quantity = models.IntegerField(verbose_name='Количество')
    date = models.DateField(verbose_name='Дата перемещения')
    worker = models.CharField(max_length=100, verbose_name='Кладовщик')

    class Meta:
        verbose_name = 'Перемещение'
        verbose_name_plural = 'Перемещения'
        ordering = ['-date']

    def __str__(self):
        return f"{self.product.name} → {self.store} ({self.quantity} шт.)"