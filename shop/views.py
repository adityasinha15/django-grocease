from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from .models import Product, Order, OrderItem
from django.contrib.sessions.models import Session
from django.template import RequestContext
import json
from django.utils import timezone




def home(request):
    beverages = Product.objects.filter(cat__category__name = 'Beverages')
    pids = Product.objects.values_list('p_id', flat=True)
    pids = list(pids)
    pids = sorted(pids)
    print(pids)
    print(beverages)
    
    return render(request, 'shop/home.html', {'beverages':beverages, 'pids':pids})

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
        try:
            if request.session['cart']:
                cart = request.session['cart']
            logout(request)
            if cart:
                request.session['cart'] = cart
            return redirect('home')
        except KeyError:
            logout(request)
            return redirect('home')
    else:
        return redirect('home')
def loginuser(request):
    if request.method == 'GET':
        return render(request, 'shop/login.html')
    else:
        user = authenticate(request, username=request.POST['email'], password=request.POST['password'])
        if user is None:
            return render(request, 'shop/login.html', {'error':'Email Id and Password did not match! Try again'})
        else:
            try:
                login(request, user)
                if request.session['cart']:
                    request.session['cart'] = request.session['cart']
                return redirect('home')
            except KeyError:
                login(request, user)
                return redirect('home')


def add_to_cart(request):
    p_id = request.GET.get('p_id')
    if request.method == 'GET':
        if 'cart' not in request.session.keys():
            request.session['cart'] = dict()
            request.session['cart'][p_id] = 1
            print(request.session['cart'])
            print(request.session.items())
            request.session.modified = True
            data = request.session['cart'][p_id]
            return HttpResponse(data)
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
            data = request.session['cart'][p_id]
            return HttpResponse(data)

def reduce_cart(request):
    try:
        p_id = request.GET.get('p_id')
        temp = request.session['cart'][p_id]
        newValue = temp-1
        request.session['cart'][p_id] = max(newValue,0) 
        request.session.modified = True
        data =request.session['cart'][p_id]
        if newValue == 0:
            del request.session['cart'][p_id]
        print(request.session['cart'])
        return HttpResponse(data)
    except KeyError:
        return render(request, 'shop/cart.html')

def increase_cart(request):
    p_id = request.GET.get('p_id')
    temp = request.session['cart'][p_id]
    newValue = temp+1
    request.session['cart'][p_id] = newValue 
    request.session.modified = True
    print(request.session['cart'])
    data = request.session['cart'][p_id]
    return HttpResponse(data)

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

def update_cart(request):
    total_items = 0
    try:
        cart = request.session['cart']
        for key in cart.keys():
            total_items += cart[key]
        return HttpResponse(total_items)
    except KeyError:
        return HttpResponse(total_items)
def delete_key(request, key=1, session='cart'):
    pass

def show_quantity_cart(request):
    p_id = request.GET.get('p_id')
    try:
        data = request.session['cart'][p_id]
        return HttpResponse(data)
    except KeyError:
        return render(request, 'shop/cart.html')

def cart(request):
    if request.method == 'GET':
        try:
            length = 0
            saves = []
            total = 0
            cart = request.session['cart']
            names = Product.objects.filter(p_id__in =cart.keys()).values_list('name', flat=True)
            prices = Product.objects.filter(p_id__in =cart.keys()).values_list('sp', flat=True)
            mrps = Product.objects.filter(p_id__in =cart.keys()).values_list('mrp', flat=True)
        
            for i in cart.keys():
                price = Product.objects.filter(p_id = i).values_list('sp', flat=True)
                length+=1
                quant = cart[i]
                tot = price[0]*quant
                total += tot
            length = range(length)
            cart = list(cart.items())
            for i in  range(len(mrps)):
                saves.append(mrps[i]-prices[i])
        
            return render(request, 'shop/cart.html', {'cart':cart, 'names':names, 'length':length, 'prices':prices, 'mrps':mrps, 'total':total})
        except KeyError:
            return HttpResponse("No items in your cart")
    else:
        if request.user.is_authenticated:
            try:
                fname = request.POST['fname']
                lname = request.POST['lname']
                address1 = request.POST['address1']
                address2 = request.POST['address2']
                city = request.POST['city']
                state = request.POST['state']
                zipcode = request.POST['zipcode']
                contact = request.POST['contact']
                cart = request.session['cart']
                grand_total = 0
                for p_id in cart.keys():
                    quantity = cart[p_id]
                    price = Product.objects.filter(p_id = p_id).values_list('sp', flat=True)
                    total = price[0] * quantity
                    grand_total += total

                order = Order(grand_total=grand_total, order_date=timezone.now() ,u_id=request.user, fname=fname, lname=lname, contact=contact, add1=address1, add2=address2, city=city, state=state, zipcode=zipcode)
                order.save()
                
                
                for p_id in cart.keys():
                    quantity = cart[p_id]
                    print(quantity)
                    price = Product.objects.filter(p_id = p_id).values_list('sp', flat=True)
                    print(price)
                    total = price[0] * quantity
                    print(total)
                    print(cart[p_id])
                    item = OrderItem(p_id=p_id, quantity=quantity, price=total)
                    item.save()
                    print(item)
                    order.items.add(item)
                    print(order.items)
                del request.session['cart']
                request.session.modified = True
                return HttpResponse('Done')
            except ValueError:
                return redirect('cart')
        else:
            return render(request, 'shop/cart.html', {'error':'Please login to proceed'})
                




