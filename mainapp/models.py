from django.db import models


class ProductCategory(models.Model):
    name = models.CharField(max_length=75, verbose_name="Name", unique=True)
    description = models.TextField(max_length=500, verbose_name="Description")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Product category"
        verbose_name_plural = "Product categories"


class Product(models.Model):
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    name = models.CharField(max_length=75, verbose_name="Name")
    image = models.ImageField(upload_to=f'products_images/{category.name}', verbose_name="Image", blank=True)
    description = models.TextField(max_length=500, verbose_name="Description", blank=True)
    price = models.DecimalField(max_digits=8, decimal_places=2, verbose_name="Price", default=0)
    quantity = models.PositiveIntegerField(verbose_name="Quantity", default=0)

    def __str__(self):
        return f"{self.category.name}: {self.name}"
