from django.urls import path
from . import views

urlpatterns = [
    path('', views.ice_cream_list, name='ice_cream_list'),  # Маршрут для ice_cream/
    path('<int:pk>/', views.ice_cream_detail, name='ice_cream_detail'),  # Маршрут для ice_cream/1/, ice_cream/2/, ...
]
