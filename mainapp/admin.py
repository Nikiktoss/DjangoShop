from django.contrib import admin
from .models import Product, ProductCategory


class ProductAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "price", "quantity")
    list_display_links = ("id", "name")


class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    list_display_links = ("id", "name")


admin.site.register(Product, ProductAdmin)
admin.site.register(ProductCategory, ProductCategoryAdmin)
