from django.shortcuts import render, redirect
from .models import *

# Create your views here.


from django.shortcuts import render
from .models import Dish

def home(request):
    popular_dishes = Dish.objects.filter(is_available=True)[:5]
    return render(request, 'home.html', {'popular_dishes': popular_dishes})


def menu(request):
    categories = Category.objects.all()
    return render(request, 'menu.html', {'categories': categories})

def add_to_cart(request, dish_id):
    dish = Dish.objects.get(id=dish_id)
    cart_item, created = CartItem.objects.get_or_create(user=request.user, dish=dish)
    cart_item.quantity += 1
    cart_item.save()
    return redirect('cart')

def cart(request):
    cart_items = CartItem.objects.filter(user=request.user)
    total_price = sum(item.get_total_price() for item in cart_items)
    return render(request, 'cart.html', {'cart_items': cart_items, 'total_price': total_price})

