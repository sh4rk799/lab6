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
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    categories = models.ManyToManyField(Category, through='ProductCategory', verbose_name='Категории')
    photo = models.ImageField(upload_to='products/', blank=True, null=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


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


class Movement(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    store = models.CharField(max_length=100)
    quantity = models.IntegerField()
    date = models.DateField()

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return f"{self.product.name} → {self.store} ({self.quantity} шт.)"






