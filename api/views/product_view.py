from django.db.models import Count
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated


from api.filters.product_filter import ProductFilter
from api.serializers.category_serializers import (
    CategorySerializer,
    CategoryRetrieveSerializer,
    CategoryListSerializer,
)
from api.serializers.product_serializers import (
    ProductSerializer,
    ProductRetrieveSerializer,
    ProductListSerializer
)

from product.models import Category, Product


class CategoryViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        if self.action in ("retrieve", "list"):
            queryset = Category.objects.prefetch_related("products")

            if self.action == "list":
                queryset = queryset.annotate(
                    product_quantity=Count("products")
                )

            return queryset
        return Category.objects.all()

    def get_serializer_class(self):
        if self.action == "retrieve":
            return CategoryRetrieveSerializer
        elif self.action == "list":
            return CategoryListSerializer
        return CategorySerializer


class ProductViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    filterset_class = ProductFilter
    http_method_names = ["get", "post", "patch", "delete"]

    def get_serializer_class(self):
        if self.action == "retrieve":
            return ProductRetrieveSerializer
        elif self.action == "list":
            return ProductListSerializer
        return ProductSerializer

    def get_queryset(self):
        if self.action == "retrieve":
            return Product.objects.select_related("category")
        return Product.objects.all()
