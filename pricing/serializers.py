from rest_framework import serializers
from .models import *

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class SeasonalProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = SeasonalProduct
        fields = '__all__'

class BulkProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = BulkProduct
        fields = '__all__'

class DiscountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Discount
        fields = '__all__'

class PercentageDiscountSerializer(serializers.ModelSerializer):
    class Meta:
        model = PercentageDiscount
        fields = '__all__'

class FixedAmountDiscountSerializer(serializers.ModelSerializer):
    class Meta:
        model = FixedAmountDiscount
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    total_price = serializers.SerializerMethodField()

    class Meta:
        model = Order
        fields = '__all__'

    def get_total_price(self, obj):
        return obj.calculate_total()
