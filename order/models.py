from django.db import models

# Create your models here.

from django.db import models
from django.contrib.auth.models import User



class Dish(models.Model):
    CATEGORY_CHOICES = [
        ('pizza', 'Пицца'),
        ('burger', 'Бургер'),
        ('salat', 'Салат')
    ]
    category = models.CharField(max_length=25, choices=CATEGORY_CHOICES)
    name = models.CharField(max_length=100)
    description = models.TextField()
    ingredients = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    is_available = models.BooleanField(default=True)
    image = models.ImageField(upload_to="dishes/", blank=True)

    

    def __str__(self):
        return self.name


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="orders")
    created_at = models.DateTimeField(auto_now_add=True)
    address = models.CharField(max_length=255)
    payment_method = models.CharField(max_length=50, choices=[('online', 'Онлайн'), ('cash', 'Готівка')])
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=[('pending', 'Очікується'), ('completed', 'Завершено')])


class CartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="cart")
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def get_total_price(self):
        return self.quantity * self.dish.price


