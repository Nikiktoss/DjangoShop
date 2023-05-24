from django.db import models
from mainapp.models import Product
from authapp.models import ShopUser


class UserBasket(models.Model):
    user = models.ForeignKey(ShopUser, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(verbose_name="Quantity", default=1)
    add_time = models.DateTimeField(verbose_name="Adding time", auto_now_add=True)
