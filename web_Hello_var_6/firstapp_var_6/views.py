from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, Movement, Category, ProductCategory
from .forms import ProductForm, MovementForm, CategoryForm

def index(request):
    products = Product.objects.all()
    movements = Movement.objects.all()

    context = {
        'page_title': 'Главная страница',
        'total_products': products.count(),
        'total_movements': movements.count(),
    }
    return render(request, 'index.html', context)

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
            return redirect('firstapp_var_6:product_list')
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
            return redirect('firstapp_var_6:product_list')
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
        return redirect('firstapp_var_6:product_list')

    return render(request, 'products/product_confirm_delete.html', {
        'product': product
    })

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
            return redirect('firstapp_var_6:movement_list')
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
            return redirect('firstapp_var_6:movement_list')
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
        return redirect('firstapp_var_6:movement_list')

    return render(request, 'movements/movement_confirm_delete.html', {
        'movement': movement
    })


def category_list(request):
    categories = Category.objects.all()
    return render(request, 'category_list.html', {
        'categories': categories,
        'page_title': 'Категории товаров'
    })


def category_create(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('firstapp_var_6:category_list')
    else:
        form = CategoryForm()

    return render(request, 'category_form.html', {
        'form': form,
        'page_title': 'Создать категорию'
    })


def category_update(request, pk):
    category = get_object_or_404(Category, pk=pk)

    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('firstapp_var_6:category_list')
    else:
        form = CategoryForm(instance=category)

    return render(request, 'category_form.html', {
        'form': form,
        'page_title': 'Редактировать категорию'
    })


def category_delete(request, pk):
    category = get_object_or_404(Category, pk=pk)

    if request.method == 'POST':
        category.delete()
        return redirect('firstapp_var_6:category_list')

    return render(request, 'category_confirm_delete.html', {
        'category': category
    })


def manage_product_categories(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    if request.method == 'POST':
        category_id = request.POST.get('category_id')

        if category_id:
            category = get_object_or_404(Category, id=category_id)
            ProductCategory.objects.get_or_create(
                product=product,
                category=category
            )

        return redirect('firstapp_var_6:manage_product_categories', product_id=product_id)

    product_categories = ProductCategory.objects.filter(product=product)
    available_categories = Category.objects.exclude(
        id__in=product_categories.values_list('category_id', flat=True)
    )

    return render(request, 'manage_product_categories.html', {
        'product': product,
        'product_categories': product_categories,
        'available_categories': available_categories,
    })

def remove_product_category(request, product_id, category_id):
    product_category = get_object_or_404(
        ProductCategory,
        product_id=product_id,
        category_id=category_id
    )
    product_category.delete()
    return redirect('firstapp_var_6:manage_product_categories', product_id=product_id)




