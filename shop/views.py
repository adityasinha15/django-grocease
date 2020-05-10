from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from .models import Product
from django.contrib.sessions.models import Session
from django.template import RequestContext





def home(request):
    beverages = Product.objects.filter(cat__category__name = 'Beverages')
    print(beverages)

    return render(request, 'shop/home.html', {'beverages':beverages, 'cart_session':request.session['cart']})

#SignUp
def signup(request):
    if request.method == 'GET':
        return render(request, 'shop/signup.html')
    else:
        if request.POST['password'] == request.POST['confirm_password']:
            try:
                user = User.objects.create_user(request.POST['email'], password=request.POST['password'], first_name=request.POST['first_name'], last_name=request.POST['last_name'])
                user.save()
                login(request, user)
                return redirect('home')
            except IntegrityError:
                return render(request, 'shop/signup.html', {'error': 'Email Id already exists! Try login'})
        else:
            return render(request, 'shop/signup.html', {'error':'Password and confirm password did not match! Try again'})

#Logout
def logoutuser(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')

def loginuser(request):
    if request.method == 'GET':
        return render(request, 'shop/login.html')
    else:
        user = authenticate(request, username=request.POST['email'], password=request.POST['password'])
        if user is None:
            return render(request, 'shop/login.html', {'error':'Email Id and Password did not match! Try again'})
        else:
            login(request, user)
            request.session['usercart'] = request.session['cart'] 
            print(request.session['usercart'])
            return redirect('home')



def add_to_cart(request):
    p_id = request.GET.get('p_id')
    if request.method == 'GET':
        if 'cart' not in request.session.keys():
            request.session['cart'] = dict()
            request.session['cart'][p_id] = 1
            print(request.session['cart'])
            print(request.session.items())
            return redirect('home')
        else:
            print(request.session['cart'])
            if has_key(request.session['cart'], p_id):
                print(request.session['cart'][p_id])
                temp = request.session['cart'].get(p_id) + 1
                print(temp)
                request.session['cart'][p_id] = temp
                request.session.modified = True
                print(request.session['cart'], 'if')
            else:
                request.session['cart'][p_id] = 1
                request.session.modified = True
                print(request.session['cart'], 'else')
            return redirect('home')



def has_key(cart , p_id):
    print(cart.keys())
    if p_id in cart.keys():
        print(cart.keys())
        return True
    else:
        return False

def delete_session(request, key='cart'):
    try:
        del request.session[key]
        return redirect('home')
    except KeyError:
        return redirect('home')
