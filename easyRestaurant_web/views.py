from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def page_first(request):
    return render(request, 'page_first.html')

def page_menu(request):
    return render(request, 'page_menu.html')

def page_test(request):
    return render(request, 'test.html')


