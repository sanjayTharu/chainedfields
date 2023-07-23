from django.contrib import admin
from .models import Product
from .forms import ProductForm
# Register your models here.

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    form= ProductForm
    list_display=['name','brand','category','price','selling_price','is_display']
    