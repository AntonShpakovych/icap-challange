from rest_framework import serializers

from product.models import Category

from api.serializers.product_serializers import ProductCompactSerializer


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["id", "name"]


class CategoryListSerializer(CategorySerializer):
    product_quantity = serializers.IntegerField(read_only=True)

    class Meta(CategorySerializer.Meta):
        fields = CategorySerializer.Meta.fields + ["product_quantity"]


class CategoryRetrieveSerializer(CategorySerializer):
    products = ProductCompactSerializer(read_only=True, many=True)

    class Meta(CategorySerializer.Meta):
        fields = CategorySerializer.Meta.fields + ["products"]
