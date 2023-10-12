from django.contrib import admin

from .models import *


# Register your models here.

admin.site.register(Restaurant)
admin.site.register(Order)
admin.site.register(Client)
admin.site.register(Plate)
admin.site.register(Section)
admin.site.register(Ingredient)
admin.site.register(Allergen)
