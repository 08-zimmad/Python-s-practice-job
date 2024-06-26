from rest_framework import serializers
from .models import Product, Category

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields="__all__"
        read_only_fields=['created_at']





class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields="__all__"