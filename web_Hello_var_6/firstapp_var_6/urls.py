from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('warehouse/', views.warehouse, name='warehouse'),
    path('shops/', views.shops, name='shops'),
    path('workers/', views.workers, name='workers'),
    path('movements/', views.movements, name='movements'),
    path('add-product/', views.add_product, name='add_product'),
    path('add-movement/', views.add_movement, name='add_movement'),
    path('view-products/', views.view_products, name='view_products'),
]