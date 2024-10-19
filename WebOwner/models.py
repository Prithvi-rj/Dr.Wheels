from django.db import models
from WebAdmin.models import *
from WebGuest.models import *
from WebOwner.models import *
from WebWorkShop.models import *
# Create your models here.

class tbl_boatdetails(models.Model):
    boat_name=models.CharField(max_length=50)
    boat_details=models.CharField(max_length=500)
    boat_rate=models.CharField(max_length=500)
    boat_capacity=models.CharField(max_length=500)
    boattype = models.ForeignKey(tbl_boattype,on_delete=models.CASCADE)
    owner = models.ForeignKey(tbl_boatowner, on_delete=models.CASCADE)
    boat_photo = models.FileField(upload_to='Assets/BoatPhoto/')
    boat_proof = models.FileField(upload_to='Assets/BoatProof/')

class tbl_requestserviceowner(models.Model):
    request_message=models.CharField(max_length=500)
    request_postdate=models.DateField(auto_now_add=True)
    request_status = models.IntegerField(default="0")
    owner = models.ForeignKey(tbl_boatowner, on_delete=models.CASCADE)
    service=models.ForeignKey(tbl_service, on_delete=models.CASCADE)