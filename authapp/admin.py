from django.contrib import admin
from django.utils.html import format_html

from .models import ShopUser, ShopUserProfile


admin.site.site_header = 'DjangoShop Administration'
admin.site.site_title = 'DjangoShop admin site'


class ShopUserAdmin(admin.ModelAdmin):
    list_display = ("id", "username", "display_photo", "is_superuser")
    list_display_links = ("id", "username")
    readonly_fields = ("display_photo",)

    def display_photo(self, obj):
        if obj.photo:
            return format_html(f'<img src="{obj.photo.url}" style="width: 80px; height: 80px"')
        else:
            return format_html(f'<img src="/static/default_images/default_user_photo.webp"'
                               f' style="width: 80px; height: 80px"')


class ShopUserProfileAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "gender")
    list_display_links = ("id", "user")


admin.site.register(ShopUser, ShopUserAdmin)
admin.site.register(ShopUserProfile, ShopUserProfileAdmin)
