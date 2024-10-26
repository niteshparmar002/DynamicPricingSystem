from rest_framework import viewsets
from .models import *
from .serializers import *

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filterset_fields = ['name','price']
    search_fields = ['name','price']
    http_method_names = ['get','post','put','patch','delete']

class SeasonalProductViewSet(viewsets.ModelViewSet):
    queryset = SeasonalProduct.objects.all()
    serializer_class = SeasonalProductSerializer
    filterset_fields = ['name','price','rate']
    search_fields = ['name','price','rate']
    http_method_names = ['get','post','put','patch','delete']

class BulkProductViewSet(viewsets.ModelViewSet):
    queryset = BulkProduct.objects.all()
    serializer_class = BulkProductSerializer
    filterset_fields = ['name','price','rate','threshold']
    search_fields = ['name','price','rate','threshold']
    http_method_names = ['get','post','put','patch','delete']

class DiscountViewSet(viewsets.ModelViewSet):
    queryset = Discount.objects.all()
    serializer_class = DiscountSerializer
    filterset_fields = ['title']
    search_fields = ['title']
    http_method_names = ['get','post','put','patch','delete']

class PercentageDiscountViewSet(viewsets.ModelViewSet):
    queryset = PercentageDiscount.objects.all()
    serializer_class = PercentageDiscountSerializer
    filterset_fields = ['title','rate']
    search_fields= ['title','rate']
    http_method_names = ['get','post','put','patch','delete']

class FixedAmountDiscountViewSet(viewsets.ModelViewSet):
    queryset = FixedAmountDiscount.objects.all()
    serializer_class = FixedAmountDiscountSerializer
    filterset_fields = ['title','amount']
    search_fields = ['title','amount']
    http_method_names = ['get','post','put','patch','delete']

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    filterset_fields = ['product','discount']
    search_fields = ['product__name','discount__title']
    http_method_names = ['get','post','put','patch','delete']
 