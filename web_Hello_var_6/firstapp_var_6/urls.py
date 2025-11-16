from django.urls import path
from . import views

app_name = 'firstapp_var_6'

urlpatterns = [
    # Главная
    path('', views.index, name='index'),
    path('warehouse/', views.warehouse, name='warehouse'),

    # Товары (функции)
    path('products/', views.product_list, name='product_list'),
    path('products/create/', views.product_create, name='product_create'),
    path('products/<int:pk>/update/', views.product_update, name='product_update'),
    path('products/<int:pk>/delete/', views.product_delete, name='product_delete'),

    # Категории (классы)
    path('categories/', views.CategoryListView.as_view(), name='category_list'),
    path('categories/create/', views.CategoryCreateView.as_view(), name='category_create'),
    path('categories/<int:pk>/update/', views.CategoryUpdateView.as_view(), name='category_update'),
    path('categories/<int:pk>/delete/', views.CategoryDeleteView.as_view(), name='category_delete'),

    # Связи товаров и категорий
    path('products/<int:product_id>/categories/',
         views.manage_product_categories, name='manage_product_categories'),
    path('products/<int:product_id>/categories/<int:category_id>/remove/',
         views.remove_product_category, name='remove_product_category'),

    # Перемещения
    path('movements/', views.movement_list, name='movement_list'),
    path('movements/create/', views.movement_create, name='movement_create'),
    path('movements/<int:pk>/update/', views.movement_update, name='movement_update'),
    path('movements/<int:pk>/delete/', views.movement_delete, name='movement_delete'),
]