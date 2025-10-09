from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'index.html')

def warehouse(request):
    return render(request, 'warehouse.html')

def shops(request):
    return render(request, 'shops.html')

def storekeeper(request):
    return render(request, 'storekeeper.html')

def table(request):
    return render(request, 'table.html')

def product1(request):
    return render(request, 'products/product1.html')

def product2(request):
    return render(request, 'products/product2.html')

def product3(request):
    return render(request, 'products/product3.html')

# Функции для магазинов
def magnit(request):
    return render(request, 'shops/magnit.html')

def dns(request):
    return render(request, 'shops/dns.html')

def pyaterochka(request):
    return render(request, 'shops/pyaterochka.html')

def mvideo(request):
    return render(request, 'shops/mvideo.html')