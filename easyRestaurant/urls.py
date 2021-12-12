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
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.page_first),
    path('test/', views.page_test),
    path('menu_promotion/', views.page_menu_promotion),
    path('menu_food/', views.page_menu_food),
    path('menu_dessert/', views.page_menu_dessert),
    path('menu_drink/', views.page_menu_drink),
    path('login/', views.page_login),
    path('register/', views.page_register),
    path('register/register_process', process.register_process),
    path('login/login_process', process.login_process),
    path('user', views.page_user),
    path('logout', process.logout),
    path('add_menu', views.add_manu),
    path('addmenu_process', process.addmenu_process),
    path('add_recommend', views.add_recommend),
    path('add_recommend_process', process.add_recommend_process),
    path('pagemenu', views.pagemenu),
    path('image_pagemenu_process', process.image_pagemenu_process),
    path('add_image_main', views.add_image_main),
    path('add_image_main_process', process.add_image_main_process),
    path('cart/addmenu<menu_id>', process.add_cart, name="add_cart"),
    path('cartdetail', process.cartdetail),
    path('cart/remove/<product_id>', process.removecart, name="removecart"),
    path('add_menu/remove/<menu_id>', process.removemenu, name="removemenu")
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
