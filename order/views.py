from django.shortcuts import render, redirect
from .models import *
from django.views.generic import ListView, DetailView

# Create your views here.

def home(request):
    #popular_dishes = Dish.objects.filter(is_available=True)[:5]
    return render(request, 'order/home.html', {'popular_dishes': 5})


class DishListView(ListView):
    model = Dish
    context_object_name = 'dishes'

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


class DishDetailView(DetailView):
    model = Dish
    context_object_name = 'dish'
