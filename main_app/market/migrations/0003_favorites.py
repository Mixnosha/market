# Generated by Django 4.0.6 on 2022-08-10 06:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0002_company_slug_product_company'),
    ]

    operations = [
        migrations.CreateModel(
            name='Favorites',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('products', models.ManyToManyField(to='market.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='market.profile')),
            ],
        ),
    ]
