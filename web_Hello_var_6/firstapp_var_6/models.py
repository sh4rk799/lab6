# models.py - ОБНОВЛЕННАЯ ВЕРСИЯ с учетом существующих данных

from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название категории')

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['name']

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=200, verbose_name='Название товара')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')

    # СОХРАНЯЕМ старое поле для обратной совместимости во время миграции
    category_old = models.CharField(max_length=100, verbose_name='Категория (старая)', blank=True)

    # НОВОЕ поле для связи многие-ко-многим
    categories = models.ManyToManyField(
        Category,
        through='ProductCategory',
        blank=True,
        verbose_name='Категории'
    )

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


class ProductCategory(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Товар')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')
    assigned_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата назначения')

    class Meta:
        verbose_name = 'Категория товара'
        verbose_name_plural = 'Категории товаров'
        unique_together = ['product', 'category']

    def __str__(self):
        return f"{self.product.name} - {self.category.name}"

# Модель Movement остается НЕИЗМЕННОЙ
class Movement(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Товар')
    store = models.CharField(max_length=100, verbose_name='Магазин')
    quantity = models.IntegerField(verbose_name='Количество')
    date = models.DateField(verbose_name='Дата перемещения')  # Убрали auto_now_add=True

    class Meta:
        verbose_name = 'Перемещение'
        verbose_name_plural = 'Перемещения'
        ordering = ['-date']

    def __str__(self):
        return f"{self.product.name} → {self.store} ({self.quantity} шт.)"