from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('restaurant/<int:restaurant_id>', views.restaurant_details, name="restaurant_details"),
    path('order/<int:restaurant_id>', views.order_from_restaurant, name="order"),
]
