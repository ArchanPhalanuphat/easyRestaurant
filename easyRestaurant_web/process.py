from django.http import HttpResponse, response
from django.contrib.auth.models import User
from django.shortcuts import render

def register_process(request):
    username=request.POST.get('username')
    firstname=request.POST.get('firstname')
    lastname=request.POST.get('lastname')
    email=request.POST.get('email')
    password=request.POST.get('password')
    repassword=request.POST.get('repassword')
    user=User.objects.create_user(
        username = username,
        password = password,
        first_name = firstname,
        last_name = lastname,
        email = email
        )
    print(username)
    user.save()
    return render(request, 'page_register.html')