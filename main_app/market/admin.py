from django.contrib import admin
from django.utils.safestring import mark_safe

from market.models import Product, Review, Manufacturer, Category, Profile, Basket

admin.site.register(Review)
admin.site.register(Category)
admin.site.register(Manufacturer)
admin.site.register(Basket)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_filter = ['product_name']
    search_fields = ['product_name']


class ProfileAdmin(admin.ModelAdmin):
    fields = ['user', 'get_image', 'profile_image', 'country', 'city',
              'address']
    readonly_fields = ('get_image',)

    def get_image(self, obj):
        return mark_safe(f'<img src="{obj.profile_image.url}" height="100px" width="100px">')


admin.site.register(Profile, ProfileAdmin)