# Generated by Django 4.0.6 on 2022-08-08 20:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_title', models.CharField(max_length=100)),
                ('slug', models.SlugField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_company', models.CharField(max_length=255)),
                ('logo', models.ImageField(upload_to='company/<django.db.models.fields.CharField>/logo')),
                ('like_rating', models.IntegerField()),
                ('location', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Delivery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('delivery', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Manufacturer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('manufacturer_name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=255)),
                ('product_price', models.DecimalField(decimal_places=2, max_digits=100)),
                ('product_description', models.TextField()),
                ('product_image', models.ImageField(upload_to='users/product_images')),
                ('availability', models.BooleanField(default=True)),
                ('sales', models.IntegerField()),
                ('slug', models.SlugField(unique=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='market.category')),
                ('product_manufacturer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='market.manufacturer')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_image', models.ImageField(blank=True, default='users/profile_images/default.jpg', null=True, upload_to='users/profile_images')),
                ('birthday', models.DateField(blank=True, null=True)),
                ('country', models.CharField(blank=True, max_length=255, null=True)),
                ('city', models.CharField(blank=True, max_length=255, null=True)),
                ('address', models.CharField(blank=True, max_length=255, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review_rating', models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)])),
                ('review_description', models.TextField(blank=True)),
                ('review_image', models.ImageField(blank=True, upload_to='users/review_images')),
                ('create_data', models.DateField(auto_now_add=True)),
                ('product_review', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='market.product')),
                ('review_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='market.profile')),
            ],
        ),
        migrations.CreateModel(
            name='BuyProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField()),
                ('delivery', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='market.delivery')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='market.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='market.profile')),
            ],
        ),
        migrations.CreateModel(
            name='Basket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=255)),
                ('amount', models.IntegerField(default=1)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='market.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='market.profile')),
            ],
        ),
    ]
