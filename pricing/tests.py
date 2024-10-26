from django.test import TestCase
from .models import *

class ProductTestCase(TestCase):
    def setUp(self):
        self.product = Product.objects.create(name="Test Product", price=100)
        self.seasonal_product = SeasonalProduct.objects.create(name="Seasonal Product", price=100, rate=10)
        self.bulk_product = BulkProduct.objects.create(name="Bulk Product", price=100, rate=20, threshold=10)

    def test_product_price(self):
        self.assertEqual(self.product.get_price(), 100)

    def test_seasonal_product_price(self):
        self.assertEqual(self.seasonal_product.get_price(), 90)

    def test_bulk_product_price(self):
        self.assertEqual(self.bulk_product.get_price(10), 800)

class DiscountTestCase(TestCase):
    def setUp(self):
        self.percentage_discount = PercentageDiscount.objects.create(title="10% off", rate=10)
        self.fixed_discount = FixedAmountDiscount.objects.create(title="20 off", amount=20)

    def test_percentage_discount(self):
        self.assertEqual(self.percentage_discount.apply_discount(100), 90)

    def test_fixed_discount(self):
        self.assertEqual(self.fixed_discount.apply_discount(100), 80)

class OrderTestCase(TestCase):
    def setUp(self):
        product = Product.objects.create(name="Order Product", price=100)
        discount = PercentageDiscount.objects.create(title="10% off", rate=10)
        self.order = Order.objects.create(product=product, quantity=2, discount=discount)

    def test_order_total(self):
        self.assertEqual(self.order.calculate_total(), 180)
