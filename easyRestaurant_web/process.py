from django.contrib import messages
from django.http import HttpResponse, response
from django.contrib.auth.models import User,auth
from django.shortcuts import redirect, render

def register_process(request):
    
    username=request.POST.get('username')
    firstname=request.POST.get('firstname')
    lastname=request.POST.get('lastname')
    email=request.POST.get('email')
    password=request.POST.get('password')
    repassword=request.POST.get('repassword')
    if password != repassword:
        messages.info(request, 'Password ไม่ถูกต้อง')
        return redirect('/register')
    elif User.objects.filter(username=username).exists():
        messages.info(request, 'username ถูกใช้ไปแล้ว')
        return redirect('/register')
    elif User.objects.filter(email=email).exists():
        messages.info(request, 'Emialนี้ถูกใช้งานไปแล้ว')
        return redirect('/register')
    else:
        user=User.objects.create_user(
        username = username,
        password = password,
        first_name = firstname,
        last_name = lastname,
        email = email
        )
    user.save()
    messages.info(request, 'สมัครสมาชิกเรียบร้อย')
    return redirect('/login')

def login_process(request):
    username=request.POST.get('username')
    password=request.POST.get('password')
    user = auth.authenticate(username=username,password=password)
    if user is not None:
        auth.login(request, user)
        return redirect('/')
    else:
        messages.info(request, 'ไม่พบข้อมูล')
        return redirect('/login')

def logout(request):
    auth.logout(request)
    return redirect('/')