from django.db import models


class Product(models.Model):
    product_name = models.CharField(max_length=255)
    product_price = models.DecimalField(decimal_places=2, max_digits=9999999)
    product_description = models.TextField()
    product_manufacturer = models.ForeignKey('Manufacturer', on_delete=models.CASCADE)
    product_review = models.ForeignKey('Review', on_delete=models.CASCADE, blank=True)
    product_image = models.ImageField(upload_to='users/product_images')

    def __str__(self):
        return self.product_name


class Review(models.Model):
    review_user = models.CharField(max_length=100)
    review_rating = models.IntegerField()
    review_description = models.TextField(blank=True)
    review_image = models.ImageField(upload_to='users/review_images', blank=True)

    def __str__(self):
        return self.review_user


class Manufacturer(models.Model):
    manufacturer_name = models.CharField(max_length=255)

    def __str__(self):
        return self.manufacturer_name



