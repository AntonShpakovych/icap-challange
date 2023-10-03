from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=20, unique=True)

    class Meta:
        ordering = ["name"]
        verbose_name_plural = "categories"

    def __str__(self) -> str:
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=255, unique=True)
    photo = models.URLField()
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

    class Meta:
        ordering = ["name"]

    def __str__(self) -> str:
        return self.name
