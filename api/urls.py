from django.urls import path, include

from rest_framework import routers
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from api.views import user_view, product_view


router = routers.DefaultRouter()

router.register(
    "categories",
    product_view.CategoryViewSet,
    basename="categories"
)
router.register(
    "products",
    product_view.ProductViewSet,
    basename="products"
)


urlpatterns = [
    path(
        "",
        include(router.urls)
    ),
    path(
        "users/register/",
        user_view.CreateUserView.as_view(),
        name="user-create"
    ),
    path(
        "users/token/",
        TokenObtainPairView.as_view(),
        name="token_obtain_pair"
    ),
    path(
        "users/token/refresh/",
        TokenRefreshView.as_view(),
        name="token_refresh"
    ),
]

app_name = "api"
