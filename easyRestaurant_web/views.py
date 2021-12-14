from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from .models import Cart, CartItem, Menu, Order, OrderItem, Table
from .models import image_promotion
from .models import image_pagemenu
from .models import image_main
# Create your views here.

def page_test(request):
    return render(request, 'test.html')

def page_first(request):
    data = image_promotion.objects.all()
    data_left = image_main.objects.all()
    return render(request, 'page_first.html', {'promotion':data,'datas':data_left})

def page_menu_promotion(request):
    data = Menu.objects.all()
    data2 = image_pagemenu.objects.all()
    return render(request, 'page_menu_promotion.html', {'menu':data,'images':data2})

def page_menu_food(request):
    data = Menu.objects.all()
    data2 = image_pagemenu.objects.all()
    return render(request, 'page_menu_food.html', {'menu':data,'images':data2})

def page_menu_dessert(request):
    data = Menu.objects.all()
    data2 = image_pagemenu.objects.all()
    return render(request, 'page_menu_dessert.html', {'menu':data,'images':data2})

def page_menu_drink(request):
    data = Menu.objects.all()
    data2 = image_pagemenu.objects.all()
    return render(request, 'page_menu_drink.html', {'menu':data,'images':data2})

def page_register(request):
    if request.user.is_authenticated:
        return redirect('/')
    else:
        return render(request, 'page_register.html')

def page_login(request):
    if request.user.is_authenticated:
        return redirect('/')
    else:
        return render(request, 'page_login.html')

def page_user(request):
    return render(request, 'page_user.html')

def add_manu(request):
    data = Menu.objects.all()
    return render(request, 'add_menu.html', {'menu':data})

def add_recommend(request):
    return render(request, 'add_recommend.html')

def pagemenu(request):
    return render(request, 'pagemenu.html')

def add_image_main(request):
    images_main = image_main.objects.all()
    images_promotion = image_promotion.objects.all()
    images_pagemenu = image_pagemenu.objects.all()
    return render(request, 'add_image_main.html', {'image_bg':images_main, 'image_promo':images_promotion, 'image_menu':images_pagemenu})

def table(request):
    data = Table.objects.all()
    return render(request, 'table.html', {'tables':data})

def table_user(request):
    data = Table.objects.all()
    return render(request, 'table_user.html ', {'tables':data})

def order(request):
    data = CartItem.objects.all()
    data2 = Cart.objects.all()
    return render(request, 'order.html', {'items':data, 'orders':data2})