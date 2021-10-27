from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
# Create your views here.

def page_test(request):
    return render(request, 'test.html')

def page_first(request):
    return render(request, 'page_first.html')

def page_menu_promotion(request):
    return render(request, 'page_menu_promotion.html')

def page_menu_food(request):
    return render(request, 'page_menu_food.html')

def page_menu_dessert(request):
    return render(request, 'page_menu_dessert.html')

def page_menu_drink(request):
    return render(request, 'page_menu_drink.html')

def page_register(request):
    print('hello')
    return render(request, 'page_register.html')



