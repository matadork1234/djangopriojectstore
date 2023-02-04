from .models import UnitMeasure, CategoryProduct, Product, Supplier
from rest_framework import viewsets, permissions, generics, status
from rest_framework.parsers import JSONParser, MultiPartParser
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import UnitMeasureSerializer, CategoryProductSerializer, ProductSerializer, SuppierSerializer

class UnitMeasureViewSet(viewsets.ModelViewSet):
    queryset = UnitMeasure.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = UnitMeasureSerializer


class CategoryProductViewSet(viewsets.ModelViewSet):
    queryset = CategoryProduct.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = CategoryProductSerializer


class ProductViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.AllowAny]
    serializer_class = ProductSerializer
    parser_classes = (JSONParser, MultiPartParser)

    def get_queryset(self):
        return Product.objects.all()
    
    @api_view(['GET'])
    def productsInventoryZero(request):
        products = Product.objects.filter(inventory = 0)
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class SupplierViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.AllowAny]
    serializer_class = SuppierSerializer

    def get_queryset(self):
        return Supplier.objects.all()

class ProductListAPIView(generics.ListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        return Product.objects.all()

class ProductCreateAPIView(generics.CreateAPIView):
    serializer_class = ProductSerializer