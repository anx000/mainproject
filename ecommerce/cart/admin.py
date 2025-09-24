from django.contrib import admin
from cart.models import Cart
from cart.models import Order
from cart.models import Order_items

admin.site.register(Cart)
# Register your models here.
admin.site.register(Order)
admin.site.register(Order_items)
