from rest_framework import serializers

from product.models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            "id",
            "name",
            "photo",
            "category",
            "is_offer_of_the_month",
            "is_available",
            "has_pickup_option",
            "description",
            "price"
        ]


class ProductListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            "id",
            "name",
            "price",
            "category"
        ]


class ProductRetrieveSerializer(ProductSerializer):
    category = serializers.CharField(source="category.name", read_only=True)


class ProductCompactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ["name", "price"]
