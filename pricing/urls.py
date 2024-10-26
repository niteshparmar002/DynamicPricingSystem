from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('products', views.ProductViewSet, basename="products")
router.register('seasonal-products', views.SeasonalProductViewSet, basename="seasonal_products")
router.register('bulk-products', views.BulkProductViewSet, basename="bulk_products")
router.register('discounts', views.DiscountViewSet, basename="discounts")
router.register('percentage-discounts', views.PercentageDiscountViewSet, basename="percentage_discounts")
router.register('fixed-amount-discounts', views.FixedAmountDiscountViewSet, basename="fixed_amount_discounts")
router.register('orders', views.OrderViewSet, basename="orders")

urlpatterns = [
    path('', include(router.urls)),
]
