from django.contrib import admin
from main.models import Product, Category, Color, Size, ProductImage



admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Color)
admin.site.register(Size)
admin.site.register(ProductImage)