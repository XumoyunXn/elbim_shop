from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.views import APIView
from .models import (
    Category,
    Product,
    ProductImage,
    Color,
    Size
)

from .serializers import (
    CategorySerializer,
    ProductSerializer,
    ProductImageSerializer,
    ColorSerializer,
    SizeSerializer,
    ProductDetailSerializer
)


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductImageViewSet(viewsets.ModelViewSet):
    queryset = ProductImage.objects.all()
    serializer_class = ProductImageSerializer


class ColorViewSet(viewsets.ModelViewSet):
    queryset = Color.objects.all()
    serializer_class = ColorSerializer


class SizeViewSet(viewsets.ModelViewSet):
    queryset = Size.objects.all()
    serializer_class = SizeSerializer




class ProductDetailAPIView(APIView):

    def get(self, request, id):

        try:
            product = Product.objects.get(id=id)

        except Product.DoesNotExist:
            return Response(
                {
                    "success": False,
                    "message": "Mahsulot topilmadi"
                },
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = ProductDetailSerializer(product)

        return Response(
            {
                "success": True,
                "data": serializer.data
            },
            status=status.HTTP_200_OK
        )