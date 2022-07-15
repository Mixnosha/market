from django.contrib import admin

from market.models import Product, Review, Manufacturer, Category

admin.site.register(Review)
admin.site.register(Category)
admin.site.register(Manufacturer)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_filter = ['product_name']
    search_fields = ['product_name']


