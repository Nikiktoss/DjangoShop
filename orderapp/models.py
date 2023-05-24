from django.db import models
from mainapp.models import Product
from authapp.models import ShopUser


class Order(models.Model):
    FORMING = "FM"
    SENT_TO_PROCEED = "STP"
    PROCEEDED = "PRD"
    PAID = "PD"
    READY = "RDY"
    CANCEL = "CNC"

    ORDER_STATUS_CHOICES = (
        (FORMING, "forming"),
        (SENT_TO_PROCEED, "sent for processing"),
        (PAID, "paid"),
        (PROCEEDED, "processed"),
        (READY, "ready"),
        (CANCEL, "canceled"),
    )

    user = models.ForeignKey(ShopUser, on_delete=models.CASCADE)
    created = models.DateTimeField(verbose_name="Date of creation", auto_now_add=True)
    updated = models.DateTimeField(verbose_name="Updated", auto_now=True)
    status = models.CharField(verbose_name="status", max_length=3, choices=ORDER_STATUS_CHOICES, default=FORMING)

    def __str__(self):
        return f"{self.user.name}:{self.status}"


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name="order_items", on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name="Product")
    quantity = models.PositiveIntegerField(verbose_name="Quantity", default=1)
