from django.shortcuts import render

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
