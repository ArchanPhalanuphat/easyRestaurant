from django.contrib import messages
from django.contrib.admin.decorators import action
from django.db.models.aggregates import Count
from django.http import HttpResponse, response
from django.contrib.auth.models import User,auth
from django.shortcuts import get_object_or_404, redirect, render
from easyRestaurant_web.models import Cart, CartItem, Menu
from easyRestaurant_web.models import image_promotion
from easyRestaurant_web.models import image_pagemenu
from easyRestaurant_web.models import image_main


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
    return redirect('/login')

def addmenu_process(request):
    name = request.POST.get('name')
    type_food = request.POST.get('type_food')
    price = request.POST.get('price')
    status = request.POST.get('status')
    if status == 'have':
        status = True
    else:
        status = False
    if len(request.FILES) != 0:
        image = request.FILES['image']
    menu=Menu(
        name = name,
        genre = type_food,
        price = price,
        status = status,
        image = image
            )
    menu.save()
    messages.info(request, 'เพิ่มเมนูเรียบร้อย')
    return redirect('/add_menu')

def add_recommend_process(request):
    name1 = request.POST.get('name1')
    price1 = request.POST.get('price1')  
    if len(request.FILES) != 0:
        image1 = request.FILES['image1']
    name2 = request.POST.get('name2')
    price2 = request.POST.get('price2')  
    if len(request.FILES) != 0:
        image2 = request.FILES['image2']
    name3 = request.POST.get('name3')
    price3 = request.POST.get('price3')  
    if len(request.FILES) != 0:
        image3 = request.FILES['image3']
    name4 = request.POST.get('name4')
    price4 = request.POST.get('price4')  
    if len(request.FILES) != 0:
        image4 = request.FILES['image4']
    image_promo = image_promotion(
        name1 = name1,
        price1 = price1,
        image1 = image1,
        name2 = name2,
        price2 = price2,
        image2 = image2,
        name3 = name3,
        price3 = price3,
        image3 = image3,
        name4 = name4,
        price4 = price4,
        image4 = image4
    )
    image_promo.save()
    messages.info(request, 'Complete')
    return redirect('/add_recommend')

def image_pagemenu_process(request):
    if len(request.FILES) != 0:
        image = request.FILES['image']
    page_menu = image_pagemenu(
        image = image
    )
    page_menu.save()
    messages.info(request, 'Complete')
    return redirect('/pagemenu')

def add_image_main_process(request):
    if len(request.FILES) != 0:
        image = request.FILES['image']
    description = request.POST.get('description')
    add_main = image_main(
        image = image,
        description = description
    )
    add_main.save()
    messages.info(request, 'complate')
    return redirect('/add_image_main')

def cartid(request):
    cart = request.session.session_key
    if not cart:
        cart = request.session.create()
    return cart

def add_cart(request, menu_id):
    product = Menu.objects.get(id=menu_id)
    try:
        cart = Cart.objects.get(cart_id=cartid(request))
    except Cart.DoesNotExist:
        cart = Cart.objects.create(cart_id=cartid(request))
        cart.save()

    try:
        cart_item = CartItem.objects.get(product=product, cart=cart)
        cart_item.quantity += 1
        cart_item.save()

    except CartItem.DoesNotExist:
        cart_item = CartItem.objects.create(
            product = product,
            cart = cart,
            quantity = 1
        )
        cart_item.save()
    return redirect('/menu_food')

def cartdetail(request):
    total = 0
    counter = 0
    cart_item = None
    try:
        cart = Cart.objects.get(cart_id=cartid(request))
        cart_item = CartItem.objects.filter(cart=cart)
        for item in cart_item:
            total += item.product.price*item.quantity
            counter += int(item.quantity)
    except Exception as e:
        pass
    return render(request, 'cartdetail.html', dict(total=total, counter=counter, cart_item=cart_item))

def removecart(request, product_id):
    cart = Cart.objects.get(cart_id=cartid(request))
    product = get_object_or_404(Menu, id=product_id)
    cartitem = CartItem.objects.get(product=product, cart=cart)
    cartitem.delete()
    return redirect('/cartdetail')