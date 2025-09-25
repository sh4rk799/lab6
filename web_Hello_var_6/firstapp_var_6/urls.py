from django.contrib import admin
from django.urls import path, include
from . import views  # ← Импорт views из текущей папки

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),  # ← Добавьте эту строку
    path('services/', views.services, name='services'),
    path('contact/', views.contact, name='contact'),
    path('news/', views.news, name='news'),
    path('portfolio/', views.portfolio, name='portfolio'),
]