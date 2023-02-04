from django.db import models
from django.core.exceptions import ValidationError
#custom validation

def validate_min_value(value):
    if (value > 1000):
        raise ValidationError('El valor no debe ser mayor a 1000')

def validate_price_product(value):
    if (value ==     0):
        raise ValidationError('El precio del producto debe ser mayor a 0')

# Create your models here.
class UnitMeasure(models.Model):
    name = models.CharField(max_length=75)
    description = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.description

class CategoryProduct(models.Model):
    name = models.CharField(max_length=150)
    description = models.CharField(max_length=350)
    order_category = models.PositiveSmallIntegerField()
    is_active = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.description


class Product(models.Model):
    name = models.TextField(max_length=100)
    description = models.TextField(max_length=5000, null=True)
    image_product = models.TextField(max_length=255, null=True)
    inventory = models.PositiveSmallIntegerField(validators=[validate_min_value])
    unit_price = models.FloatField(default=0, validators=[validate_price_product])
    code_product = models.CharField(max_length=25)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now= True)
    unit_measure= models.ForeignKey(UnitMeasure, on_delete = models.RESTRICT)
    category_product = models.ForeignKey(CategoryProduct, on_delete = models.RESTRICT)


class Supplier(models.Model):
    full_name = models.CharField(max_length=150)
    number_document_identity = models.CharField(max_length=20)
    institution = models.CharField(max_length=500)
    job_position = models.CharField(max_length=500)
    address_institution = models.CharField(max_length=250)
    is_active = models.BooleanField(default= True)

class EntryOrderStore(models.Model):
    number_order = models.PositiveIntegerField()
    invoice_number = models.CharField(max_length=35)
    total_price_order = models.FloatField(default=0)
    code_string = models.TextField(max_length=5000)
    date_register_order = models.DateTimeField(auto_now_add = True)
    date_updated_order = models.DateTimeField(auto_now = True)
    supplier = models.ForeignKey(Supplier, on_delete= models.RESTRICT)

class DetailOrderEntry(models.Model):
    quantity = models.PositiveIntegerField()
    price = models.FloatField(default=0)
    product = models.ForeignKey(Product, on_delete=models.RESTRICT)
    entry_order = models.ForeignKey(EntryOrderStore, on_delete = models.CASCADE)