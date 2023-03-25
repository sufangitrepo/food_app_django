from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .views import (
    CategoryView,
    add_category,
    get_categories,
    add_product,
    get_products,
    ProductView,
   

    )

urlpatterns = [
    path('category/<int:id>' , CategoryView.as_view()),
    path('addCategory/' , add_category),
    path('categories/' , get_categories),


    path('addProduct/' , add_product),
    path('products' , get_products),
    path('deleteProduct/<int:id>' , ProductView.as_view()),
    
    
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)