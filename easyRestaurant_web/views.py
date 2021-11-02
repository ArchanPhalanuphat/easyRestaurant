from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from .models import Menu
# Create your views here.

def page_test(request):
    return render(request, 'test.html')

def page_first(request):
    return render(request, 'page_first.html')

def page_menu_promotion(request):
    return render(request, 'page_menu_promotion.html')

def page_menu_food(request):
    data = Menu.objects.all()
    return render(request, 'page_menu_food.html', {'menu':data})

def page_menu_dessert(request):
    data = Menu.objects.all()
    return render(request, 'page_menu_dessert.html', {'menu':data})

def page_menu_drink(request):
    data = Menu.objects.all()
    return render(request, 'page_menu_drink.html', {'menu':data})

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
    return render(request, 'add_menu.html')


