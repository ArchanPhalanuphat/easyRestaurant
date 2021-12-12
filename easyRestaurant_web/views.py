from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from .models import Menu
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
    return render(request, 'add_image_main.html')

