from django_filters import rest_framework as filters

from product.models import Product


class ProductFilter(filters.FilterSet):
    category = filters.CharFilter(field_name="category__name")

    class Meta:
        model = Product
        fields = [
            "category",
            "is_offer_of_the_month",
            "is_available",
            "has_pickup_option"
        ]
