# Generated by Django 4.0.6 on 2022-08-10 06:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0003_favorites'),
    ]

    operations = [
        migrations.AlterField(
            model_name='favorites',
            name='products',
            field=models.ManyToManyField(null=True, to='market.product'),
        ),
    ]