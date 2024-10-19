from django.shortcuts import render,redirect
from WebGuest.models import *
from WebWorkShop.models import *
from WebUser.models import *
# Create your views here.

def homepage(request):
    return render(request,"Mechanic/HomePage.html")

def logout(request):
    del request.session["wid"]
    return redirect("Mechanic:Login")

def my_pro(request):
    data=tbl_mechanic.objects.get(id=request.session["mid"])
    return render(request,"Mechanic/MyProfile.html",{'data':data})

def editprofile(request):
    prodata=tbl_mechanic.objects.get(id=request.session["mid"])
    if request.method=="POST":
        prodata.mechanic_name=request.POST.get('txtname')
        prodata.mechanic_contact=request.POST.get('txtcon')
        prodata.mechanic_email=request.POST.get('txtemail')
        prodata.save()
        return render(request,"Mechanic/EditProfile.html",{'msg':"Profile Updated"})
    else:
        return render(request,"Mechanic/EditProfile.html",{'prodata':prodata})

def changepassword(request):
    if request.method=="POST":
        ccount=tbl_mechanic.objects.filter(id=request.session["mid"],mechanic_password=request.POST.get('txtcurpass')).count()
        if ccount>0:
            if request.POST.get('txtnewpass')==request.POST.get('txtconpass'):
                userdata=tbl_mechanic.objects.get(id=request.session["mid"],mechanic_password=request.POST.get('txtcurpass'))
                userdata.mechanic_password=request.POST.get('txtnewpass')
                userdata.save()
                return render(request,"Mechanic/ChangePassword.html",{'msg':"Password Updated"})
            else:
                return render(request,"Mechanic/ChangePassword.html",{'msg1':"Error in confirm Password"})
        else:
            return render(request,"Mechanic/ChangePassword.html",{'msg1':"Error in current password"})
    else:
        return render(request,"Mechanic/ChangePassword.html")




def requestServiceListAssigned(request):
    provider=tbl_mechanic.objects.get(id=request.session["mid"])
    userdata = tbl_requestservice.objects.filter(request_status=4,mechanic=provider)
    return render(request,"Mechanic/ServiceListAssigned.html",{"userdata":userdata})

def completerequest(request,rid):
    user = tbl_requestservice.objects.get(id=rid)
    user.request_status = 3
    user.save()
    return redirect("Mechanic:homepage")




def requestServiceListCompleted(request):
    provider=tbl_mechanic.objects.get(id=request.session["mid"])
    userdata = tbl_requestservice.objects.filter(request_status=3,mechanic=provider)
    return render(request,"Mechanic/ServiceListCompleted.html",{"userdata":userdata})



