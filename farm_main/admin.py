from django.contrib import admin

from . models import Category, Product


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug','description']
    list_editable = ['description']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Category,  CategoryAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'stock', 'available', 'updated', 'created']
    list_editable = ['price', 'stock', 'available']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Product, ProductAdmin)

