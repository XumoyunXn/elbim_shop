from django.db import models




class Category(models.Model):
    img = models.ImageField(upload_to='img/')
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name




class Product(models.Model):
    name = models.CharField(max_length=255)

    description = models.TextField(
        blank=True
    )

    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name="products"
    )

    def __str__(self):
        return self.name


class ProductImage(models.Model):
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name="images"
    )

    image = models.ImageField(
        upload_to="products/"
    )

    def __str__(self):
        return f"{self.product.name} - {self.id}"


class Color(models.Model):
    name = models.CharField(
        max_length=50
    )

    hex_code = models.CharField(
        max_length=7
    )

    products = models.ManyToManyField(
        Product,
        related_name="colors"
    )

    def __str__(self):
        return self.name


class Size(models.Model):
    name = models.CharField(
        max_length=20
    )

    products = models.ManyToManyField(
        Product,
        related_name="sizes"
    )

    def __str__(self):
        return self.name