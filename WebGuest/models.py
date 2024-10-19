from django.db import models
from WebAdmin.models import *
# Create your models here.
class tbl_user(models.Model):
    user_name=models.CharField(max_length=50)
    user_gender=models.CharField(max_length=50)
    user_contact=models.CharField(max_length=50)
    user_email=models.CharField(max_length=50)
    user_password=models.CharField(max_length=50)
    place = models.ForeignKey(tbl_place, on_delete=models.CASCADE)
    user_photo = models.FileField(upload_to='Assets/UserPhoto/')
    user_proof = models.FileField(upload_to='Assets/UserProof/')
    user_status = models.IntegerField(default="0")


class tbl_boatowner(models.Model):
    owner_name=models.CharField(max_length=50)
    owner_gender=models.CharField(max_length=50)
    owner_contact=models.CharField(max_length=50)
    owner_email=models.CharField(max_length=50)
    owner_address=models.CharField(max_length=500)
    owner_about=models.CharField(max_length=500)
    owner_password=models.CharField(max_length=50)
    place = models.ForeignKey(tbl_place, on_delete=models.CASCADE)
    owner_photo = models.FileField(upload_to='Assets/OwnerPhoto/')
    owner_proof = models.FileField(upload_to='Assets/OwnerProof/')
    owner_status = models.IntegerField(default="0")
    owner_doj=models.DateField(auto_now_add=True)
    
class tbl_shop(models.Model):
    shop_name=models.CharField(max_length=50)
    shop_contact=models.CharField(max_length=50)
    shop_email=models.CharField(max_length=50)
    shop_address=models.CharField(max_length=500)
    shop_about=models.CharField(max_length=500)
    shop_password=models.CharField(max_length=50)
    place = models.ForeignKey(tbl_place, on_delete=models.CASCADE)
    shop_photo = models.FileField(upload_to='Assets/ShopPhoto/')
    shop_proof = models.FileField(upload_to='Assets/ShopProof/')
    shop_status = models.IntegerField(default="0")
    shop_doj=models.DateField(auto_now_add=True)
    
class tbl_workshop(models.Model):
    workshop_name=models.CharField(max_length=50)
    workshop_contact=models.CharField(max_length=50)
    workshop_email=models.CharField(max_length=50)
    workshop_address=models.CharField(max_length=500)
    workshop_about=models.CharField(max_length=500)
    workshop_password=models.CharField(max_length=50)
    place = models.ForeignKey(tbl_place, on_delete=models.CASCADE)
    workshop_photo = models.FileField(upload_to='Assets/WorkShopPhoto/')
    workshop_proof = models.FileField(upload_to='Assets/WorkShopProof/')
    workshop_status = models.IntegerField(default="0")
    workshop_doj=models.DateField(auto_now_add=True)
    