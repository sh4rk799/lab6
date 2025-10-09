from django.contrib import admin
from django.urls import path, include
from . import views  # ← Импорт views из текущей папки

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('warehouse/', views.warehouse, name='warehouse'),  # ← Добавьте эту строку
    path('shops/', views.shops, name='shops'),
    path('storekeeper/', views.storekeeper, name='storekeeper'),
    path('table/', views.table, name='table'),
    # Товары
    path('warehouse/product1/', views.product1),
    path('warehouse/product2/', views.product2),
    path('warehouse/product3/', views.product3),

    # Магазины
    path('shops/magnit/', views.magnit),
    path('shops/dns/', views.dns),
    path('shops/pyaterochka/', views.pyaterochka),
    path('shops/mvideo/', views.mvideo),
    ]