from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('homepage.urls')),  # Подключаем urls приложения homepage
    path('about/', include('about.urls')),  # Подключаем urls приложения about
]
