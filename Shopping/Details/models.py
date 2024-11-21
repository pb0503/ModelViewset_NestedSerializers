from django.db import models

# Create your models here.
class Product(models.Model):
    product_id=models.IntegerField()
    product_name=models.CharField(max_length=50)
    price=models.FloatField()

class Comment(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    comment=models.TextField()
    rating=models.IntegerField()