from django.shortcuts import render, redirect

from .models import Restaurant

from django.shortcuts import get_object_or_404

# Create your views here.
def index(request):
    context = {}
    context['restaurants'] = Restaurant.objects.all()

    return render(request, 'orders/index.html', context)


def restaurant_details(request, restaurant_id):
    context = {}
    restaurant = get_object_or_404(Restaurant, pk=restaurant_id)
    context['restaurant'] = restaurant

    return render(request, 'orders/restaurant.html', context)

def order_from_restaurant(request, restaurant_id): #
    context = {}

    restaurant = get_object_or_404(Restaurant, pk=restaurant_id)
    context['restaurant'] = restaurant

    if request.POST:
        #post logic to create order
        pass

    return render(request, 'orders/order_from_restaurant.html', context)