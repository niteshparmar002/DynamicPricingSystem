from django.contrib import admin
from .models import *

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name','price']
    search_fields = ['name']

class SeasonalProductAdmin(admin.ModelAdmin):
    list_display = ['name','price','rate']
    search_fields = ['name']

class BulkProductAdmin(admin.ModelAdmin):
    list_display = ['name','price','rate','threshold']
    search_fields = ['name']

class DiscountAdmin(admin.ModelAdmin):
    list_display = ['title']
    search_fields = ['title']

class PercentageDiscountAdmin(admin.ModelAdmin):
    list_display = ['title','rate']
    search_fields = ['title']

class FixedAmountDiscountAdmin(admin.ModelAdmin):
    list_display = ['title','amount']
    search_fields = ['title']

class OrderAdmin(admin.ModelAdmin):
    list_display = ['product','discount','quantity']
    search_fields = ['product__name','discount__title']
    autocomplete_fields = ['product','discount']

admin.site.register(Product, ProductAdmin)
admin.site.register(SeasonalProduct, SeasonalProductAdmin)
admin.site.register(BulkProduct, BulkProductAdmin)
admin.site.register(Discount, DiscountAdmin)
admin.site.register(PercentageDiscount, PercentageDiscountAdmin)
admin.site.register(FixedAmountDiscount, FixedAmountDiscountAdmin)
admin.site.register(Order, OrderAdmin)
