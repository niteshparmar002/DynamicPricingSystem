from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def get_price(self, quantity=1):
        return self.price * quantity

    class Meta:
        verbose_name_plural = "01. Product"

    def __str__(self):
        return f"{self.name} - ${self.price}"

class SeasonalProduct(Product):
    rate = models.DecimalField(max_digits=5, decimal_places=2, default=0, verbose_name="Seasonal Discount Rate")

    def get_price(self):
        discount = self.price * (self.rate / 100)
        return self.price - discount
    
    class Meta:
        verbose_name_plural = "02. Seasonal Product"

class BulkProduct(Product):
    rate = models.DecimalField(max_digits=5, decimal_places=2, default=0, verbose_name="Bulk Discount Rate")
    threshold = models.IntegerField(default=10, verbose_name="Bulk Threshold")

    def get_price(self, quantity=1):
        price = self.price
        if quantity >= self.threshold:
            price -= self.price * (self.rate / 100)
        return price * quantity

    class Meta:
        verbose_name_plural = "03. Bulk Product"

class Discount(models.Model):
    title = models.CharField(max_length=100)

    def apply_discount(self, price):
        return price
    
    class Meta:
        verbose_name_plural = "04. Discount"
    
    def __str__(self):
        return self.title

class PercentageDiscount(Discount):
    rate = models.DecimalField(max_digits=5, decimal_places=2)

    def apply_discount(self, price):
        return price - (price * (self.rate / 100))

    class Meta:
        verbose_name_plural = "05. Percentage Discount"

class FixedAmountDiscount(Discount):
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    def apply_discount(self, price):
        return price - self.amount
    
    class Meta:
        verbose_name_plural = "06. Fixed Amount Discount"

class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.PROTECT, related_name="order_product")
    discount = models.ForeignKey(Discount, on_delete=models.PROTECT, related_name="order_discount", null=True, blank=True)
    quantity = models.IntegerField()

    def calculate_total(self):
        price = self.product.get_price(self.quantity)
        if self.discount:
            return self.discount.apply_discount(price)
        return price
    
    class Meta:
        verbose_name_plural = "07. Order"

    def __str__(self):
        return f"Order of {self.quantity} {self.product.name}(s) - Total: ${self.calculate_total()}"
