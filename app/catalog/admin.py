from django.contrib import admin

from app.catalog.models import Category, Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['pk','title']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['pk','title', 'price', 'category']

