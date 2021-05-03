from django.contrib import admin
from .models import (
    Product,
    Review,
    Order,
    OrderItem,
    ShippingAddress,
)


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']


class OrderAdmin(admin.ModelAdmin):
    list_display = ['_id', 'user', 'isDelivered', 'deliveredAt']


admin.site.register(Product, ProductAdmin)
admin.site.register(Review)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem)
admin.site.register(ShippingAddress)
