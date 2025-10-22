from django.shortcuts import render
from .forms import ProductForm
import csv

def read_file(filename):
    data = []
    try:
        with open(f'templates/tablica/{filename}', 'r', encoding='utf-8') as file:
            for line in file:
                if line.strip():
                    data.append(line.strip().split(';'))
    except:
        pass
    return data


def read_csv_file():
    data = []
    try:
        with open('templates/tablica/movements.csv', 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                data.append(row)
    except:
        pass
    return data


def index(request):
    products = read_file('products.txt')
    movements = read_csv_file()

    context = {
        'page_title': 'Главная страница',
        'total_products': len(products),
        'total_movements': len(movements),
        'last_movement': movements[-1] if movements else {'Товар': 'нет данных', 'Магазин': 'нет данных'}
    }
    return render(request, 'index.html', context)


def warehouse(request):
    products = read_file('products.txt')
    movements = read_csv_file()

    simple_data = {
        'total_count': len(products),
        'warehouse_name': 'Основной склад',
        'is_active': True,
        'area': 500,
        'total_movements': len(movements)
    }

    complex_data = {
        'products_list': products,
        'categories': list(set([p[3] for p in products])) if products else [],
        'movements_list': movements,
    }

    context = {
        'simple': simple_data,
        'complex': complex_data,
        'page_title': 'Склад товаров'
    }
    return render(request, 'warehouse.html', context)


def shops(request):
    stores = read_file('stores.txt')
    movements = read_csv_file()

    store_stats = {}
    for movement in movements:
        store = movement['Магазин']
        quantity = int(movement['Количество'])
        if store in store_stats:
            store_stats[store] += quantity
        else:
            store_stats[store] = quantity

    context = {
        'simple': {
            'stores_count': len(stores),
            'city': 'Москва'
        },
        'complex': {
            'stores_list': stores,
            'store_stats': store_stats,
        },
        'page_title': 'Магазины-получатели'
    }
    return render(request, 'shops.html', context)


def movements(request):
    movements_data = read_csv_file()

    context = {
        'movements_list': movements_data,
        'page_title': 'Перемещения товаров',
        'total_count': len(movements_data)
    }
    return render(request, 'movements.html', context)


def workers(request):
    workers_data = read_file('workers.txt')
    movements = read_csv_file()

    worker_stats = {}
    for movement in movements:
        worker = movement['Кладовщик']
        quantity = int(movement['Количество'])
        if worker in worker_stats:
            worker_stats[worker] += quantity
        else:
            worker_stats[worker] = quantity

    context = {
        'workers_list': workers_data,
        'worker_stats': worker_stats,
        'page_title': 'Кладовщики'
    }
    return render(request, 'workers.html', context)


def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            price = form.cleaned_data['price']
            quantity = form.cleaned_data['quantity']
            category = form.cleaned_data['category']

            # Записываем в файл
            with open('templates/tablica/products.txt', 'a', encoding='utf-8') as f:
                f.write(f"\n{name};{price};{quantity};{category}")

            context = {
                'message': f'Добавлен: {name} - {price} руб., {quantity} шт., {category}',
                'page_title' : 'Успех'
            }

            return render(request, 'success.html', context)
    else:
        form = ProductForm()

    context = {
        'form' : form,
        'page_title' : 'Добавить товар'
    }

    return render(request, 'add_product.html', context)