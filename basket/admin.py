from django.contrib import admin
from .models import UserBasket


class UserBasketAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "product")
    list_display_links = ("id", "user")


admin.site.register(UserBasket, UserBasketAdmin)
