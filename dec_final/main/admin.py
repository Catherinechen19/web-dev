from django.contrib import admin
from .models import Product
# from .models import Categories

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'qty', 'category', 'product_price']

    def product_price(self, obj):
        return "Rp. {}".format(obj.price)

    list_filter = ['category']
    search_fields = ['name']
    filter_horizontal = ()



admin.site.register(Product, ProductAdmin)

# class CategoryAdmin(admin.ModelAdmin):
#     list_display = ['user', 'category']

# admin.site.register(Categories, CategoryAdmin)

