from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('warehouse/', views.warehouse, name='warehouse'),
    path('shops/', views.shops, name='shops'),
    path('workers/', views.workers, name='workers'),
    path('movements/', views.movements, name='movements'),
]
