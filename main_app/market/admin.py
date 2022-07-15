from django.contrib import admin

from market.models import Product, Review, Manufacturer

admin.site.register(Review)
admin.site.register(Manufacturer)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_filter = ['product_name']
    search_fields = ['product_name']
    fields = ['product_name', 'product_price', 'product_description', 'product_review', 'product_manufacturer', 'product_image']


