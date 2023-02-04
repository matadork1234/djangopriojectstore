from django.contrib import admin

from .models import CategoryProduct, DetailOrderEntry, EntryOrderStore, Product, Supplier, UnitMeasure

# Register your models here.

class CategoryProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

class UnitMeasureAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'inventory', 'unit_price', 'code_product', 'is_active', 'unit_measure', 'category_product')   

admin.site.register(CategoryProduct, CategoryProductAdmin)
admin.site.register(DetailOrderEntry)
admin.site.register(EntryOrderStore)
admin.site.register(Product, ProductAdmin)
admin.site.register(Supplier)
admin.site.register(UnitMeasure, UnitMeasureAdmin)