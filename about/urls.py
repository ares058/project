from django.urls import path
from . import views  # Импортируем views.py

urlpatterns = [
    path('', views.description, name='description'),  # Маршрут для /about/
]
