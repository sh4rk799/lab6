from django.shortcuts import render, redirect, get_object_or_404
from .models import Product, Movement
from .forms import ProductForm, MovementForm


# Главная страница
def index(request):
    products = Product.objects.all()
    movements = Movement.objects.all()

    context = {
        'page_title': 'Главная страница',
        'total_products': products.count(),
        'total_movements': movements.count(),
        'last_movement': movements.last() if movements.exists() else None
    }
    return render(request, 'index.html', context)


# CRUD для товаров (Задание 2.2)
def product_list(request):
    products = Product.objects.all()
    return render(request, 'products/product_list.html', {
        'products': products,
        'page_title': 'Товары'
    })


def product_create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm()

    return render(request, 'products/product_form.html', {
        'form': form,
        'page_title': 'Добавить товар',
        'action': 'create'
    })


def product_update(request, pk):
    product = get_object_or_404(Product, pk=pk)

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm(instance=product)

    return render(request, 'products/product_form.html', {
        'form': form,
        'page_title': 'Редактировать товар',
        'action': 'update'
    })


def product_delete(request, pk):
    product = get_object_or_404(Product, pk=pk)

    if request.method == 'POST':
        product.delete()
        return redirect('product_list')

    return render(request, 'products/product_confirm_delete.html', {
        'product': product
    })


# CRUD для перемещений (Задание 2.1)
def movement_list(request):
    movements = Movement.objects.all()
    return render(request, 'movements/movement_list.html', {
        'movements': movements,
        'page_title': 'Перемещения'
    })


def movement_create(request):
    if request.method == 'POST':
        form = MovementForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('movement_list')
    else:
        form = MovementForm()

    return render(request, 'movements/movement_form.html', {
        'form': form,
        'page_title': 'Добавить перемещение',
        'action': 'create'
    })


def movement_update(request, pk):
    movement = get_object_or_404(Movement, pk=pk)

    if request.method == 'POST':
        form = MovementForm(request.POST, instance=movement)
        if form.is_valid():
            form.save()
            return redirect('movement_list')
    else:
        form = MovementForm(instance=movement)

    return render(request, 'movements/movement_form.html', {
        'form': form,
        'page_title': 'Редактировать перемещение',
        'action': 'update'
    })


def movement_delete(request, pk):
    movement = get_object_or_404(Movement, pk=pk)

    if request.method == 'POST':
        movement.delete()
        return redirect('movement_list')

    return render(request, 'movements/movement_confirm_delete.html', {
        'movement': movement
    })


# Склад - показывает товары и перемещения из БД
def warehouse(request):
    products = Product.objects.all()
    movements = Movement.objects.all()

    context = {
        'products': products,
        'movements': movements[:5],  # Последние 5 перемещений
        'page_title': 'Склад товаров',
        'total_products': products.count(),
        'total_movements': movements.count(),
        'categories': list(set(products.values_list('category', flat=True))),
    }
    return render(request, 'warehouse.html', context)
