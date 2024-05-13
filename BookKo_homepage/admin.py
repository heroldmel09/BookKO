from django.contrib import admin
from .models import *





# Register your models here.
admin.site.register(Customer)
admin.site.register(Books)
admin.site.register(YourOrder)
admin.site.register(OrderItemCart)
admin.site.register(Shipping_Address)
admin.site.register(Books_Sale)