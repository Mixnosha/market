from django.conf import settings
from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class Product(models.Model):
    product_name = models.CharField(max_length=255)
    product_price = models.DecimalField(decimal_places=2, max_digits=100)
    product_description = models.TextField()
    product_manufacturer = models.ForeignKey('Manufacturer', on_delete=models.CASCADE)
    product_image = models.ImageField(upload_to='users/product_images')
    availability = models.BooleanField(default=True)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    sales = models.IntegerField()
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.product_name

    def get_absolute_url(self):
        return reverse('one_product', kwargs={'slug': self.slug})


class Review(models.Model):
    RATING_CHOICES = [
        (1, 1), (2, 2), (3, 3), (4, 4), (5, 5)
    ]
    review_user = models.ForeignKey('Profile', on_delete=models.CASCADE)
    review_rating = models.IntegerField(choices=RATING_CHOICES)
    review_description = models.TextField(blank=True)
    review_image = models.ImageField(upload_to='users/review_images', blank=True)
    product_review = models.ForeignKey('Product', on_delete=models.CASCADE)
    create_data = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.review_user.user.username}: {self.product_review.product_name}'


class Category(models.Model):
    category_title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=50, unique=True)

    def __str__(self):
        return self.category_title


class Manufacturer(models.Model):
    manufacturer_name = models.CharField(max_length=255)

    def __str__(self):
        return self.manufacturer_name


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    profile_image = models.ImageField(upload_to='users/profile_images', null=True, blank=True, default='users/profile_images/default.jpg')
    birthday = models.DateField(blank=True, null=True)
    country = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=255, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.user.username


class Basket(models.Model):
    user = models.ForeignKey('Profile', on_delete=models.CASCADE)
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    status = models.CharField(max_length=255)
    amount = models.IntegerField(default=1)

    def __str__(self):
        return f'{self.user}  product:   {self.product.product_name}'


class Delivery(models.Model):
    delivery = models.CharField(max_length=255)

    def __str__(self):
        return self.delivery


class BuyProduct(models.Model):
    user = models.ForeignKey('Profile', on_delete=models.CASCADE)
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    delivery = models.ForeignKey('Delivery', on_delete=models.CASCADE, null=True)
    amount = models.IntegerField()

    def __str__(self):
        return f'{self.user}  buy:   {self.product.product_name}'

class Company(models.Model):
    name_company = models.CharField(max_length=255)
    logo = models.ImageField(upload_to=f'company/{name_company}/logo')
    like_rating = models.IntegerField()
    location = models.CharField(max_length=255)

    def __str__(self):
        return self.name_company