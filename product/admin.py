from django.contrib import admin

from product.models import Category, Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "category",
        "is_offer_of_the_month",
        "is_available",
        "has_pickup_option",
    )
    list_filter = (
        "category",
        "is_offer_of_the_month",
        "is_available",
        "has_pickup_option",
    )
    search_fields = ("name", "description")


admin.site.register(Category)
