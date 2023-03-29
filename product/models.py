from django.db import models
from app_authentication.models import AppUser

class Category(models.Model):
    category_name = models.CharField(unique=True, max_length=100)
    


class Product(models.Model):
    product_name = models.CharField( max_length=100)
    qty = models.IntegerField(default=0)
    category = models.ForeignKey(to=Category, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=100, decimal_places=3)
    description = models.CharField(max_length=200)
    image = models.ImageField()


    
class FavouriteProducts(models.Model):
    user = models.ForeignKey(to=AppUser, on_delete=models.CASCADE)
    product = models.ForeignKey(to=Product, on_delete=models.CASCADE)
    
