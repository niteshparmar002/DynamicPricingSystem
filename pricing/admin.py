from django.contrib import admin
from .models import *

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name','price']
    list_display = ['name']

class SeasonalProductAdmin(admin.ModelAdmin):
    list_display = ['name','price','rate']
    list_display = ['name']

class BulkProductAdmin(admin.ModelAdmin):
    list_display = ['name','price','rate','threshold']
    list_display = ['name']

class DiscountAdmin(admin.ModelAdmin):
    list_display = ['title']
    list_display = ['title']

class PercentageDiscountAdmin(admin.ModelAdmin):
    list_display = ['title','rate']
    list_display = ['title']

class FixedAmountDiscountAdmin(admin.ModelAdmin):
    list_display = ['title','rate']
    list_display = ['title']

class OrderAdmin(admin.ModelAdmin):
    list_display = ['product','discount','quantity']
    list_display = ['product__name','discount__title']
    autocomplete_fields = ['product','discount']

admin.site.register(Product)
admin.site.register(SeasonalProduct)
admin.site.register(BulkProduct)
admin.site.register(Discount)
admin.site.register(PercentageDiscount)
admin.site.register(FixedAmountDiscount)
admin.site.register(Order)
