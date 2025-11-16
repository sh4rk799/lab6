from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('warehouse/', views.warehouse, name='warehouse'),
    # path('shops/', views.shops, name='shops'),
    # path('workers/', views.workers, name='workers'),
    # path('movements/', views.movements, name='movements'),
    # path('view-products/', views.view_products, name='view_products'),

    # CRUD для товаров
    path('products/', views.product_list, name='product_list'),
    path('products/create/', views.product_create, name='product_create'),
    path('products/<int:pk>/update/', views.product_update, name='product_update'),
    path('products/<int:pk>/delete/', views.product_delete, name='product_delete'),

    # CRUD для перемещений
    path('movements-db/', views.movement_list, name='movement_list'),
    path('movements-db/create/', views.movement_create, name='movement_create'),
    path('movements-db/<int:pk>/update/', views.movement_update, name='movement_update'),
    path('movements-db/<int:pk>/delete/', views.movement_delete, name='movement_delete'),
]