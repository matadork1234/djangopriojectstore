from django.urls import path, include
from rest_framework import routers
from .api import UnitMeasureViewSet, CategoryProductViewSet, ProductViewSet,SupplierViewSet, ProductListAPIView, ProductCreateAPIView

router = routers.DefaultRouter()

router.register('api/unit-measure', UnitMeasureViewSet, 'unit-measure')
router.register('api/category-product', CategoryProductViewSet, 'category-product')
router.register('api/product', ProductViewSet, 'product')
router.register('api/supplier', SupplierViewSet, 'supplier')


urlpatterns = [    
    path('', include(router.urls)),
    path('products', ProductViewSet.productsInventoryZero, name='products-zero')
]
    #path('api/product2/', ProductListAPIView.as_view(), name = 'product_list'),
    #path('api/product2/create', ProductCreateAPIView.as_view(), name = 'product_create')

