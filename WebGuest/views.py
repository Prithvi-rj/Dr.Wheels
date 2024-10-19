from django.shortcuts import render,redirect
from WebAdmin.models import *
from WebGuest.models import *
from WebWorkShop.models import *
# Create your views here.

def index(request):
    return render(request,"WebGuest/index.html")

def userRegistration(request):
    district = tbl_district.objects.all()
    if request.method=="POST":
        place = tbl_place.objects.get(id=request.POST.get('sel_place'))
        tbl_user.objects.create(user_name=request.POST.get("txtname"),user_gender=request.POST.get("gender"),user_contact=request.POST.get("txtcontact"),user_email=request.POST.get("txtemail"),user_photo=request.FILES.get("fileImage"),user_proof=request.FILES.get("fileProof"),user_password=request.POST.get("txtpwd"),place=place)
        return redirect("WebGuest:userRegistration")
    else:
        return render(request,"WebGuest/NewUser.html",{"districtdata":district})

def ownerRegistration(request):
    district = tbl_district.objects.all()
    if request.method=="POST":
        place = tbl_place.objects.get(id=request.POST.get('sel_place'))
        tbl_boatowner.objects.create(owner_address=request.POST.get("txtadd"),owner_about=request.POST.get("txtabout"),owner_name=request.POST.get("txtname"),owner_gender=request.POST.get("gender"),owner_contact=request.POST.get("txtcontact"),owner_email=request.POST.get("txtemail"),owner_photo=request.FILES.get("fileImage"),owner_proof=request.FILES.get("fileProof"),owner_password=request.POST.get("txtpwd"),place=place)
        return redirect("WebGuest:ownerRegistration")
    else:
        return render(request,"WebGuest/NewOwner.html",{"districtdata":district})

def shopRegistration(request):
    district = tbl_district.objects.all()
    if request.method=="POST":
        place = tbl_place.objects.get(id=request.POST.get('sel_place'))
        tbl_shop.objects.create(shop_address=request.POST.get("txtadd"),shop_about=request.POST.get("txtabout"),shop_name=request.POST.get("txtname"),shop_contact=request.POST.get("txtcontact"),shop_email=request.POST.get("txtemail"),shop_photo=request.FILES.get("fileImage"),shop_proof=request.FILES.get("fileProof"),shop_password=request.POST.get("txtpwd"),place=place)
        return redirect("WebGuest:shopRegistration")
    else:
        return render(request,"WebGuest/NewShop.html",{"districtdata":district})

def workshopRegistration(request):
    district = tbl_district.objects.all()
    if request.method=="POST":
        place = tbl_place.objects.get(id=request.POST.get('sel_place'))
        tbl_workshop.objects.create(workshop_address=request.POST.get("txtadd"),workshop_about=request.POST.get("txtabout"),workshop_name=request.POST.get("txtname"),workshop_contact=request.POST.get("txtcontact"),workshop_email=request.POST.get("txtemail"),workshop_photo=request.FILES.get("fileImage"),workshop_proof=request.FILES.get("fileProof"),workshop_password=request.POST.get("txtpwd"),place=place)
        return redirect("WebGuest:workshopRegistration")
    else:
        return render(request,"WebGuest/NewWorkShop.html",{"districtdata":district})

def ajaxplace(request):
    dis = tbl_district.objects.get(id=request.GET.get("did"))
    place = tbl_place.objects.filter(district=dis)
    return render(request,"WebGuest/AjaxPlace.html",{"placedata":place})

def Login(request):
    if request.method == "POST":

        admincount = tbl_admin.objects.filter(admin_email=request.POST.get("txt_email"),admin_password=request.POST.get("txt_password")).count()
        usercount = tbl_user.objects.filter(user_email=request.POST.get("txt_email"),user_password=request.POST.get("txt_password")).count()
        shopcount = tbl_shop.objects.filter(shop_status='1',shop_email=request.POST.get("txt_email"),shop_password=request.POST.get("txt_password")).count()
        workshopcount = tbl_workshop.objects.filter(workshop_status='1',workshop_email=request.POST.get("txt_email"),workshop_password=request.POST.get("txt_password")).count()
        mcount = tbl_mechanic.objects.filter(mechanic_status='1',mechanic_email=request.POST.get("txt_email"),mechanic_password=request.POST.get("txt_password")).count()
        
        if usercount > 0:
            user = tbl_user.objects.get(user_email=request.POST.get("txt_email"),user_password=request.POST.get("txt_password"))
            request.session["uid"] = user.id
            request.session["uname"] = user.user_name
            return redirect("WebUser:homepage")
        elif admincount > 0:
            admin = tbl_admin.objects.get(admin_email=request.POST.get("txt_email"),admin_password=request.POST.get("txt_password"))
            request.session["aid"] = admin.id
            request.session["aname"] = admin.admin_name
            return redirect("WebAdmin:LoadingHomePage")
        elif mcount > 0:
            mech = tbl_mechanic.objects.get(mechanic_email=request.POST.get("txt_email"),mechanic_password=request.POST.get("txt_password"))
            request.session["mid"] = mech.id
            return redirect("Mechanic:homepage")
        elif shopcount > 0:
            shop = tbl_shop.objects.get(shop_email=request.POST.get("txt_email"),shop_password=request.POST.get("txt_password"))
            request.session["sid"] = shop.id
            return redirect("WebShop:homepage")
        elif workshopcount > 0:
            workshop = tbl_workshop.objects.get(workshop_email=request.POST.get("txt_email"),workshop_password=request.POST.get("txt_password"))
            request.session["wid"] = workshop.id
            return redirect("WebWorkShop:homepage")
        else:
            return render(request,"WebGuest/Login.html",{"msg":"Invalid Email Or Password"})
    else:
        return render(request,"WebGuest/Login.html")