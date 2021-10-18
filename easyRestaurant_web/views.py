from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def page_first(request):
    return render(request, 'page_first.html')
