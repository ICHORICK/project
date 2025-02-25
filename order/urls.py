from django.urls import path
from order import views

urlpatterns = [
    path('', views.DishListView.as_view(), name="dish-list"),
    path('<int:pk>/', views.DishDetailView.as_view(), name="dish-detail"),
]