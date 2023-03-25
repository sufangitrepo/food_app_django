from django.db import models

class Category(models.Model):
    category_name = models.CharField(unique=True, max_length=100)
    


class Product(models.Model):
    product_name = models.CharField(unique=True, max_length=100)
    qty = models.IntegerField(default=0)
    category = models.ForeignKey(to=Category, on_delete=models.CASCADE)
    manufacture_date = models.DateTimeField(null=True)
    image = models.ImageField(upload_to='productImages')


    
