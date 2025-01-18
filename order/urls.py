from django.urls import path
from order import views

urlpatterns = [
    path("restaran", views.home, name="restaran"),
    path("menu/", views.menu, name="menu")
]