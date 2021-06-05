from django.contrib import admin

from .models import Supplier, Product


class SupplierAdmin(admin.ModelAdmin):
    admin.site.register(Supplier)


class ProductAdmin(admin.ModelAdmin):
    admin.site.register(Product)