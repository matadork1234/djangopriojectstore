from django.contrib.auth.models import User
from rest_framework import serializers
from .models import UnitMeasure, CategoryProduct, Product, EntryOrderStore, DetailOrderEntry, Supplier


class UnitMeasureSerializer(serializers.ModelSerializer):
    class Meta:
        model = UnitMeasure
        fields = '__all__'
        

class CategoryProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryProduct
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    #unit_measure = UnitMeasureSerializer(read_only=True)
    #category_product = CategoryProductSerializer(read_only=True)

    class Meta:
        model = Product
        exclude = ('created_at', 'updated_at')
      
        #fields = ('id', 'name', 'description', 'image_product', 'inventory', 'unit_price', 'code_product', 'is_active', 'created_at', 'updated_at', 'unit_measure', 'category_product')
    def to_representation(self,instance):
        return {
            'id': instance.id,
            'name': instance.name,
            'description': instance.description,
            'image_product': instance.image_product,
            'inventory': instance.inventory,
            'unit_price': instance.unit_price,            
            'code_product': instance.code_product,
            'is_active': instance.is_active,
            'unit_measure': instance.unit_measure.description if instance.unit_measure is not None else '',
            'category_product': instance.category_product.description if instance.category_product is not None else ''
        }
    
    

class SuppierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = '__all__'

class EntryOrderStoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = EntryOrderStore
        fields = '__all__'

class DetailOrderEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = DetailOrderEntry
        fields = '__all__'