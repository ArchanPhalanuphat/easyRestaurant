"""easyRestaurant URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from easyRestaurant_web import process, views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.page_first),
    path('test/', views.page_test),
    path('menu_promotion/', views.page_menu_promotion),
    path('menu_food/', views.page_menu_food),
    path('menu_dessert/', views.page_menu_dessert),
    path('menu_drink/', views.page_menu_drink),
    path('register/', views.page_register),
    path('register/register_process/', process.register_process),
]
