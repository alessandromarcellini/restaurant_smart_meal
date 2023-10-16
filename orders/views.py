from django.shortcuts import render

from .models import Restaurant

# Create your views here.



def restaurant(request, restaurant_id):
    context = {}

    if request.user.is_authenticated:
        pass
    restaurant = Restaurant.objects.get(restaurant_id=restaurant_id)
    context['restaurant'] = restaurant

    return render(request, 'orders/restaurant.html', context)
