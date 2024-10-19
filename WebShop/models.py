from django.db import models
from WebAdmin.models import *
from WebGuest.models import *
# Create your models here.
class tbl_product(models.Model):
    product_name=models.CharField(max_length=50)
    product_details=models.CharField(max_length=50)
    product_rate=models.CharField(max_length=50)
    subcat = models.ForeignKey(tbl_subcategory, on_delete=models.CASCADE)
    brand = models.ForeignKey(tbl_brand, on_delete=models.CASCADE)
    shop = models.ForeignKey(tbl_shop, on_delete=models.CASCADE)
    product_photo = models.FileField(upload_to='Assets/ProductPhoto/')
    product_stock = models.IntegerField(default=0)


class tbl_productstock(models.Model):
    product = models.ForeignKey(tbl_product, on_delete=models.CASCADE)
    stock_qty = models.IntegerField(default=0)
    stock_date = models.DateField(auto_now_add=True)