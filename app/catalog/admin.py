from django.contrib import admin

from app.catalog.models import Category, Product, Contact


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['pk','title']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['pk','title', 'price', 'category']

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['pk', 'name', 'phone', 'message']
