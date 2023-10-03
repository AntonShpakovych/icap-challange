from django.db import models

from product.utils import path_for_product_image


class Category(models.Model):
    name = models.CharField(max_length=20)

    class Meta:
        verbose_name_plural = "categories"


class Product(models.Model):
    name = models.CharField(max_length=255)
    photo = models.ImageField(
        upload_to=path_for_product_image,
        null=True,
        blank=True
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name="products"
    )
    is_offer_of_the_month = models.BooleanField(default=False)
    is_available = models.BooleanField(default=True)
    has_pickup_option = models.BooleanField(default=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name
