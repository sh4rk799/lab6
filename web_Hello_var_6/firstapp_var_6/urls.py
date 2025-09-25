from django.contrib import admin
from django.urls import path, include
from . import views  # ← Импорт views из текущей папки

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('warehouse/', views.warehouse, name='warehouse'),  # ← Добавьте эту строку
    path('shops/', views.shops, name='shops'),
    path('storekeeper/', views.storekeeper, name='storekeeper'),
    path('table/', views.table, name='table'),]