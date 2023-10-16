from django.urls import path

from . import views

urlpatterns = [
    path('restaurant/<int:restaurant_id>', views.restaurant, name="restaurant"),
]
