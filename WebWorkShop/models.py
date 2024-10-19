from django.db import models
from WebAdmin.models import *
from WebGuest.models import *


class tbl_service(models.Model):
    service_name=models.CharField(max_length=50)
    service_details=models.CharField(max_length=500)
    service_rate=models.CharField(max_length=500)
    servicetype = models.ForeignKey(tbl_servicetype, on_delete=models.CASCADE)
    workshop=models.ForeignKey(tbl_workshop, on_delete=models.CASCADE)

class tbl_mechanic(models.Model):
    mechanic_name=models.CharField(max_length=50)
    mechanic_contact=models.CharField(max_length=50)
    mechanic_email=models.CharField(max_length=50)
    mechanic_password=models.CharField(max_length=50)
    place = models.ForeignKey(tbl_place, on_delete=models.CASCADE)
    mechanic_photo = models.FileField(upload_to='Assets/MechDocs/')
    mechanic_proof = models.FileField(upload_to='Assets/MechDocs/')
    mechanic_status = models.IntegerField(default="0")
    workshop=models.ForeignKey(tbl_workshop, on_delete=models.CASCADE)
