from django.urls import path
from auth_sys import views

urlpatterns = [
    path('login/', views.CustomLoginView.as_view(), name="login"),
    path('register/', views.register_view, name="register")
]