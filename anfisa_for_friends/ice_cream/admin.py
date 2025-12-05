from django.contrib import admin

from .models import Category, Topping, IceCream, Wrapper


admin.site.register(Category)
admin.site.register(Topping)
admin.site.register(IceCream)
admin.site.register(Wrapper)
