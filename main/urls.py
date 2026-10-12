from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import (
    CategoryViewSet,
    ProductViewSet,
    ProductImageViewSet,
    ColorViewSet,
    SizeViewSet,
    ProductDetailAPIView,
)


router = DefaultRouter()

router.register(
    "categories",
    CategoryViewSet,
    basename="category"
)

router.register(
    "products",
    ProductViewSet,
    basename="product"
)

router.register(
    "product-images",
    ProductImageViewSet,
    basename="product-image"
)

router.register(
    "colors",
    ColorViewSet,
    basename="color"
)

router.register(
    "sizes",
    SizeViewSet,
    basename="size"
)


urlpatterns = [
    # ViewSet API'lar
    path("", include(router.urls)),

    # Bitta mahsulot haqida to'liq ma'lumot
    path(
        "products/detail/<int:id>/",
        ProductDetailAPIView.as_view(),
        name="product-detail",
    ),
]