from django.contrib import admin
from .models import Product


# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'price', 'stock', 'category', 'modified_date', 'is_available')
    prepopulate_fields = {'slug': ('product_slug',)}

admin.site.register(Product, ProductAdmin)
