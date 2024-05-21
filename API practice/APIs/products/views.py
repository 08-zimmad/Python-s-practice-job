from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Product, Category
from .serializers import ProductSerializer, CategorySerializers
from rest_framework import status


class ProductsAPI(APIView):
    def get(self,request,pk=None):  # what is format here
        if pk is not None:
            products=Product.objects.filter(id=pk)
            if not products.exists():
                return Response({"error": "Object Not Found"}, status=status.HTTP_404_NOT_FOUND)            
            product_serializer=ProductSerializer(products.first())
            return Response(product_serializer.data)
        products=Product.objects.all()
        product_serializer=ProductSerializer(products, many=True)
        return Response(product_serializer.data)
    

    def post(self, request):
        data=request.data
        product_serializer=ProductSerializer(data=data)
        if product_serializer.is_valid():
            product_serializer.save()
            return Response({"msg":"Data Saved"}, status=status.HTTP_201_CREATED)
        return Response(product_serializer.error_messages, status=status.HTTP_400_BAD_REQUEST)
    

    def patch(self,request,pk):
        product=Product.objects.filter(id=pk)
        if product.exists():
            product_serializer=ProductSerializer(product.first(),data=request.data, partial=True)
            if product_serializer.is_valid():
                product_serializer.save()
                return Response({'msg':"Product Updated"}, status=status.HTTP_200_OK)
            return Response(product_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({'error':"Selected Product Not Found"},status=status.HTTP_404_NOT_FOUND)
    


    def delete(self,request,pk):
        pass




class CategoryAPI(APIView):
    pass
