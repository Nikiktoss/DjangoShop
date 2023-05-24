from django.contrib import admin
from .models import Order, OrderItem


class OrderAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "created", "updated")
    list_display_links = ("id", "user")


class OrderItemAdmin(admin.ModelAdmin):
    list_display = ("id", "order", "product")
    list_display_links = ("id", "order")


admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem, OrderItemAdmin)
