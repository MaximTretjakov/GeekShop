from django.contrib import admin
from .models import ProductCategory, Product


class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    ordering = ['name']


admin.site.register(ProductCategory, ProductCategoryAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = ('category', 'name', 'image', 'short_desc', 'description', 'price', 'quantity')
    ordering = ['name']


admin.site.register(Product, ProductAdmin)
