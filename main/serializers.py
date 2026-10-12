from rest_framework import serializers
from .models import (
    Category,
    Product,
    ProductImage,
    Color,
    Size
)


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = [
            "id",
            "img",
            "name",
        ]


class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = [
            "id",
            "image",
        ]


class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Color
        fields = [
            "id",
            "name",
            "hex_code",
        ]


class SizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Size
        fields = [
            "id",
            "name",
        ]


class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    images = ProductImageSerializer(many=True, read_only=True)
    colors = ColorSerializer(many=True, read_only=True)
    sizes = SizeSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = [
            "id",
            "name",
            "description",
            "category",
            "images",
            "colors",
            "sizes",
        ]


class ProductDetailSerializer(serializers.ModelSerializer):

    category = CategorySerializer(read_only=True)

    images = ProductImageSerializer(
        many=True,
        read_only=True
    )

    colors = ColorSerializer(
        many=True,
        read_only=True
    )

    sizes = SizeSerializer(
        many=True,
        read_only=True
    )

    class Meta:
        model = Product
        fields = [
            "id",
            "name",
            "description",
            "category",
            "images",
            "colors",
            "sizes"
        ]