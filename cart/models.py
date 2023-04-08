from django.db import models
from app_authentication.models import AppUser
from product.models import Product

class Cart(models.Model):

    user = models.OneToOneField(to=AppUser, on_delete=models.CASCADE)
    total = models.DecimalField(max_digits=30, decimal_places=2, default=0.0, )
    sub_total = models.DecimalField(max_digits=30, decimal_places=2, default=0.0,)



    

class CartItem(models.Model):

    cart = models.ForeignKey(to=Cart, on_delete=models.CASCADE)
    qty  = models.IntegerField()
    date = models.DateTimeField(auto_created=True, auto_now=True)
    product = models.OneToOneField(to=Product, on_delete=models.CASCADE)
    amount = models.DecimalField(decimal_places=2, max_digits=20, default=0.0)
    



