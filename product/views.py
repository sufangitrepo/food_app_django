from django.http import HttpRequest
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from .serializers import (
    CategorySerilaizer,
    ProductSerializer,
)

from .models import (
    Category,
    Product,
    )



RESPONSE = 'response'
ERROR = 'error'



@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAdminUser])
def add_category(request: HttpRequest) -> Response:
        category_serializer = CategorySerilaizer(data=request.data)
        category_serializer.is_valid(raise_exception=True)
        category: Category = category_serializer.save()
        return Response({RESPONSE: 'category added successfully', 'category_id': category.id })



@api_view(['GET'])
def get_categories(request: HttpRequest)-> Response:
    categories = Category.objects.all()
    category_serializer: CategorySerilaizer = CategorySerilaizer(categories, many=True)
    return Response(category_serializer.data)


class CategoryView(APIView):
    
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAdminUser]

    def patch(self, request: HttpRequest, id)-> Response:
        category: Category = None

        try:
             category = Category.objects.get(id=id) 
        except ObjectDoesNotExist :
             return Response({ERROR: 'Category not found with this id',}, status= status.HTTP_404_NOT_FOUND)
        
        if category:
            category_serializer = CategorySerilaizer(category,data=request.data, partial=True)
            category_serializer.is_valid(raise_exception=True)
            updated_category = category = category_serializer.save()
            return Response({RESPONSE: 'updated sucessfully', 'category_id':updated_category.id})
       

    def delete(self, request: HttpRequest, id)-> Response:
        
        try:
             category: Category = Category.objects.get(id=id) 
             category.delete()
             return Response({RESPONSE: 'category delete successfully', "category_id":id})
        except ObjectDoesNotExist :
             return Response({ERROR: 'Category not found with this id',}, status= status.HTTP_404_NOT_FOUND)



@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAdminUser])
def add_product(request: HttpRequest)-> Response:
    product_serializer = ProductSerializer(data=request.data)
    product_serializer.is_valid(raise_exception=True)
    product: Product = product_serializer.save()
    return Response(data={RESPONSE: 'product added successfully', 'product_id': product.id})


@api_view(['GET'])
def get_products(request: HttpRequest):
    product_name = request.query_params.get('productName')
    category = request.query_params.get('category')
    products = None
    if product_name:
        products = Product.objects.filter(product_name__contains=product_name)
    elif category:
        products = Product.objects.filter(category=category)
    else: 
        products = Product.objects.all()
    
    product_serializer = ProductSerializer(products, many=True)
    return Response(product_serializer.data)



class ProductView(APIView):
     
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAdminUser]


    def delete(self, request: HttpRequest, id):
        product: Product = None
        try:
            product = Product.objects.get(id=id)
        except ObjectDoesNotExist:
            return Response({ERROR: 'product does not exist'}, status=status.HTTP_404_NOT_FOUND)

        if product:
            product.delete()
            return Response({RESPONSE: 'product deleted successfully', })    

         



    



