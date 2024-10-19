from django.shortcuts import render,redirect
from WebGuest.models import *
from WebWorkShop.models import *
from WebUser.models import *
# Create your views here.

def homepage(request):
    return render(request,"WebWorkShop/HomePage.html")

def logout(request):
    del request.session["wid"]
    return redirect("WebGuest:Login")

def my_pro(request):
    data=tbl_workshop.objects.get(id=request.session["wid"])
    return render(request,"WebWorkShop/MyProfile.html",{'data':data})

def editprofile(request):
    prodata=tbl_workshop.objects.get(id=request.session["wid"])
    if request.method=="POST":
        prodata.workshop_name=request.POST.get('txtname')
        prodata.workshop_contact=request.POST.get('txtcon')
        prodata.workshop_email=request.POST.get('txtemail')
        prodata.save()
        return render(request,"WebWorkShop/EditProfile.html",{'msg':"Profile Updated"})
    else:
        return render(request,"WebWorkShop/EditProfile.html",{'prodata':prodata})

def changepassword(request):
    if request.method=="POST":
        ccount=tbl_workshop.objects.filter(id=request.session["wid"],workshop_password=request.POST.get('txtcurpass')).count()
        if ccount>0:
            if request.POST.get('txtnewpass')==request.POST.get('txtconpass'):
                userdata=tbl_workshop.objects.get(id=request.session["wid"],workshop_password=request.POST.get('txtcurpass'))
                userdata.workshop_password=request.POST.get('txtnewpass')
                userdata.save()
                return render(request,"WebWorkShop/ChangePassword.html",{'msg':"Password Updated"})
            else:
                return render(request,"WebWorkShop/ChangePassword.html",{'msg1':"Error in confirm Password"})
        else:
            return render(request,"WebWorkShop/ChangePassword.html",{'msg1':"Error in current password"})
    else:
        return render(request,"WebWorkShop/ChangePassword.html")


#
def ServiceDetails(request):
    category = tbl_servicetype.objects.all()
    provider=tbl_workshop.objects.get(id=request.session["wid"])
    data = tbl_service.objects.filter(workshop=provider)
    if request.method=="POST":
        category = tbl_servicetype.objects.get(id=request.POST.get('sel_type'))
        tbl_service.objects.create(service_details=request.POST.get("txtdetails"),service_name=request.POST.get("txtname"),service_rate=request.POST.get("txtscale"),servicetype=category,workshop=provider)
        return redirect("WebWorkShop:ServiceDetails")
    else:
        return render(request,"WebWorkShop/ServiceDetails.html",{"category":category,"data":data})


def deleteServiceDetails(request,did):
    tbl_service.objects.get(id=did).delete()
    return redirect("WebWorkShop:ServiceDetails")


#
def requestServiceList(request):
    provider=tbl_workshop.objects.get(id=request.session["wid"])
    userdata = tbl_requestservice.objects.filter(request_status=0,service__workshop=provider)
    return render(request,"WebWorkShop/ServiceListRequested.html",{"userdata":userdata})

def acceptrequest(request,aid):
    user = tbl_requestservice.objects.get(id=aid)
    user.request_status = 1
    user.save()
    return redirect("WebWorkShop:homepage")

def AssignNowRequest(request,asid):
    rData = tbl_requestservice.objects.get(id=asid)
    provider=tbl_workshop.objects.get(id=request.session["wid"])
    mdata=tbl_mechanic.objects.filter(workshop=provider)
    if request.method=="POST":
        rData.request_status=4
        mech = tbl_mechanic.objects.get(id=request.POST.get('selMech'))
        rData.mechanic=mech
        rData.save()
        return redirect("WebWorkShop:homepage")
    else:
        return render(request,"WebWorkShop/AssignNowRequest.html",{"userdata":rData,"mdata":mdata})

def rejectrequest(request,rid):
    user = tbl_requestservice.objects.get(id=rid)
    user.request_status = 2
    user.save()
    return redirect("WebWorkShop:homepage")

def completerequest(request,rid):
    user = tbl_requestservice.objects.get(id=rid)
    user.request_status = 3
    user.save()
    return redirect("WebWorkShop:homepage")

def requestServiceListAccepted(request):
    provider=tbl_workshop.objects.get(id=request.session["wid"])
    userdata = tbl_requestservice.objects.filter(request_status=1,service__workshop=provider)
    return render(request,"WebWorkShop/ServiceListAccepted.html",{"userdata":userdata})

def requestServiceListAssigned(request):
    provider=tbl_workshop.objects.get(id=request.session["wid"])
    userdata = tbl_requestservice.objects.filter(request_status=4,service__workshop=provider)
    return render(request,"WebWorkShop/ServiceListAssigned.html",{"userdata":userdata})


def requestServiceListRejected(request):
    provider=tbl_workshop.objects.get(id=request.session["wid"])
    userdata = tbl_requestservice.objects.filter(request_status=2,service__workshop=provider)
    return render(request,"WebWorkShop/ServiceListRejected.html",{"userdata":userdata})


def requestServiceListCompleted(request):
    provider=tbl_workshop.objects.get(id=request.session["wid"])
    userdata = tbl_requestservice.objects.filter(request_status=3,service__workshop=provider)
    return render(request,"WebWorkShop/ServiceListCompleted.html",{"userdata":userdata})


def NewMechanic(request):
    district = tbl_district.objects.all()
    provider=tbl_workshop.objects.get(id=request.session["wid"])
    if request.method=="POST":
        place = tbl_place.objects.get(id=request.POST.get('sel_place'))
        tbl_mechanic.objects.create(workshop=provider,mechanic_name=request.POST.get("txtname"),mechanic_contact=request.POST.get("txtcontact"),mechanic_email=request.POST.get("txtemail"),mechanic_photo=request.FILES.get("fileImage"),mechanic_proof=request.FILES.get("fileProof"),mechanic_password=request.POST.get("txtpwd"),place=place)
        return redirect("WebWorkShop:NewMechanic")
    else:
        return render(request,"WebWorkShop/NewMechanic.html",{"districtdata":district})


def ajaxplace(request):
    dis = tbl_district.objects.get(id=request.GET.get("did"))
    place = tbl_place.objects.filter(district=dis)
    return render(request,"WebWorkShop/AjaxPlace.html",{"placedata":place})



def MechaniList(request):
    userdata = tbl_mechanic.objects.filter(mechanic_status=0)
    return render(request,"WebWorkShop/MechaniList.html",{"userdata":userdata})

def acceptmechanic(request,aid):
    user = tbl_mechanic.objects.get(id=aid)
    user.mechanic_status = 1
    user.save()
    return redirect("WebWorkShop:homepage")

def rejectmechanic(request,rid):
    user = tbl_mechanic.objects.get(id=rid)
    user.mechanic_status = 2
    user.save()
    return redirect("WebWorkShop:homepage")

def MechanicListAccepted(request):
    userdata = tbl_mechanic.objects.filter(mechanic_status=1)
    return render(request,"WebWorkShop/MechanicListAccepted.html",{"userdata":userdata})

def MechanicListRejected(request):
    userdata = tbl_mechanic.objects.filter(mechanic_status=2)
    return render(request,"WebWorkShop/MechanicListRejected.html",{"userdata":userdata})