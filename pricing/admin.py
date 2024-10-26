from django.contrib import admin
from .models import *

admin.site.register(Product)
admin.site.register(SeasonalProduct)
admin.site.register(BulkProduct)
admin.site.register(Discount)
admin.site.register(PercentageDiscount)
admin.site.register(FixedAmountDiscount)
admin.site.register(Order)
