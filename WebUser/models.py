from django.db import models
from WebGuest.models import *
from WebWorkShop.models import *
from WebShop.models import *
from WebOwner.models import *


class tbl_complaint(models.Model):
    complaint_title=models.CharField(max_length=500)
    complaint_details=models.CharField(max_length=500)
    complaint_postdate=models.DateField(auto_now_add=True)
    complaint_reply=models.CharField(max_length=500)
    complaint_replydate=models.DateField(null=True)
    complaint_status = models.IntegerField(default="0")
    user = models.ForeignKey(tbl_user, on_delete=models.CASCADE,null=True)
   

class tbl_feedback(models.Model):
    feedback_subject=models.CharField(max_length=500)
    feedback_details=models.CharField(max_length=500)
    feedback_postdate=models.DateField(auto_now_add=True)
    feedback_status = models.IntegerField(default="0")
    user = models.ForeignKey(tbl_user, on_delete=models.CASCADE)

class tbl_requestservice(models.Model):
    request_message=models.CharField(max_length=500)
    request_postdate=models.DateField(auto_now_add=True)
    request_status = models.IntegerField(default="0")
    user = models.ForeignKey(tbl_user, on_delete=models.CASCADE)
    service=models.ForeignKey(tbl_service, on_delete=models.CASCADE)
    mechanic=models.ForeignKey(tbl_mechanic, on_delete=models.CASCADE,null=True)


class tbl_requestboat(models.Model):
    request_message=models.CharField(max_length=500)
    request_todate=models.CharField(max_length=500,null=True)
    request_postdate=models.DateField(auto_now_add=True)
    request_status = models.IntegerField(default="0")
    user = models.ForeignKey(tbl_user, on_delete=models.CASCADE)
    boat=models.ForeignKey(tbl_boatdetails, on_delete=models.CASCADE)
    
class tbl_booking(models.Model):
    booking_status = models.IntegerField(default=0)
    booking_amount = models.CharField(max_length=30)
    boking_date = models.DateField(auto_now_add=True)
    user = models.ForeignKey(tbl_user, on_delete=models.CASCADE,null=True)
    owner = models.ForeignKey(tbl_boatowner, on_delete=models.CASCADE,null=True)

class tbl_cart(models.Model):
    cart_qty = models.IntegerField(default=1)
    product = models.ForeignKey(tbl_product, on_delete=models.CASCADE)
    booking = models.ForeignKey(tbl_booking, on_delete=models.CASCADE)
    cart_status = models.IntegerField(default=0)