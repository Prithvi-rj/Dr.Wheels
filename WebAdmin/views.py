from django.shortcuts import render,redirect
from WebAdmin.models import *
from WebGuest.models import *
from WebUser.models import *
from datetime import date
# Create your views here.

def LoadingHomePage(request):
    return render(request,"WebAdmin/HomePage.html")



def districtInsertSelect(request):
    dis=tbl_district.objects.all()
    if request.method=="POST":
        disName=request.POST.get('txtname')
        tbl_district.objects.create(district_name=disName)
        return redirect("WebAdmin:districtInsertSelect")
    else:
        return render(request,"WebAdmin/District.html",{'data':dis})

def delDistrict(request,did):
    tbl_district.objects.get(id=did).delete()
    return redirect("WebAdmin:districtInsertSelect")

def districtupdate(request,eid):
    editdata=tbl_district.objects.get(id=eid)
    if request.method=="POST":
        editdata.district_name=request.POST.get("txtname")
        editdata.save()
        return redirect("WebAdmin:districtInsertSelect")
    else:
        return render(request,"WebAdmin\District.html",{"editdata":editdata})


def placeInsertSelect(request):
    district = tbl_district.objects.all()
    data=tbl_place.objects.all()
    if request.method=="POST":
        placeName=request.POST.get('txtname')
        dis = tbl_district.objects.get(id=request.POST.get('sel_district'))
        tbl_place.objects.create(place_name=placeName,district=dis)
        return redirect("WebAdmin:placeInsertSelect")
    else:
        return render(request,"WebAdmin/Place.html",{'data':data,"districtdata":district})

def delPlace(request,did):
    tbl_place.objects.get(id=did).delete()
    return redirect("WebAdmin:placeInsertSelect")

def placeupdate(request,eid):
    district = tbl_district.objects.all()
    editdata=tbl_place.objects.get(id=eid)
    if request.method=="POST":
        editdata.place_name=request.POST.get("txtname")
        dis = tbl_district.objects.get(id=request.POST.get('sel_district'))
        editdata.district = dis
        editdata.save()
        return redirect("WebAdmin:placeInsertSelect")
    else:
        return render(request,"WebAdmin\Place.html",{"editdata":editdata,"districtdata":district})


def adminInsertSelect(request):
    data=tbl_admin.objects.all()
    if request.method=="POST":
        name=request.POST.get('txtname')
        contact=request.POST.get('txtcontact')
        email=request.POST.get('txtemail')
        pwd=request.POST.get('txtpwd')
        tbl_admin.objects.create(admin_name=name,admin_contact=contact,admin_email=email,admin_password=pwd)
        return redirect("WebAdmin:adminInsertSelect")
    else:
        return render(request,"WebAdmin/AdminRegistration.html",{'data':data})

def delAdminReg(request,did):
    tbl_admin.objects.get(id=did).delete()
    return redirect("WebAdmin:adminInsertSelect")

def adminRegUpdate(request,eid):
    editdata=tbl_admin.objects.get(id=eid)
    if request.method=="POST":
        editdata.admin_name=request.POST.get("txtname")
        editdata.admin_contact=request.POST.get("txtcontact")
        editdata.admin_email=request.POST.get("txtemail")
        editdata.admin_password=request.POST.get("txtpwd")
        editdata.save()
        return redirect("WebAdmin:adminInsertSelect")
    else:
        return render(request,"WebAdmin\AdminRegistration.html",{"editdata":editdata})


def userListNew(request):
    userdata = tbl_user.objects.filter(user_status=0)
    return render(request,"WebAdmin/UserListNew.html",{"userdata":userdata})



#owner

def OwnerListNew(request):
    userdata = tbl_boatowner.objects.filter(owner_status=0)
    return render(request,"WebAdmin/OwnerListNew.html",{"userdata":userdata})

def acceptowner(request,aid):
    user = tbl_boatowner.objects.get(id=aid)
    user.owner_status = 1
    user.save()
    return redirect("WebAdmin:LoadingHomePage")

def rejectowner(request,rid):
    user = tbl_boatowner.objects.get(id=rid)
    user.owner_status = 2
    user.save()
    return redirect("WebAdmin:LoadingHomePage")

def OwnerListAccepted(request):
    userdata = tbl_boatowner.objects.filter(owner_status=1)
    return render(request,"WebAdmin/OwnerListAccepted.html",{"userdata":userdata})

def OwnerListRejected(request):
    userdata = tbl_boatowner.objects.filter(owner_status=2)
    return render(request,"WebAdmin/OwnerListRejected.html",{"userdata":userdata})


#Master Entry
def CategoryInsertSelect(request):
    data=tbl_category.objects.all()
    if request.method=="POST":
        catName=request.POST.get('txtname')
        tbl_category.objects.create(category_name=catName)
        return redirect("WebAdmin:CategoryInsertSelect")
    else:
        return render(request,"WebAdmin/Category.html",{'data':data})

def delCategory(request,did):
    tbl_category.objects.get(id=did).delete()
    return redirect("WebAdmin:CategoryInsertSelect")

def Categoryupdate(request,eid):
    editdata=tbl_category.objects.get(id=eid)
    if request.method=="POST":
        editdata.category_name=request.POST.get("txtname")
        editdata.save()
        return redirect("WebAdmin:CategoryInsertSelect")
    else:
        return render(request,"WebAdmin\Category.html",{"editdata":editdata})



def SubCatInsertSelect(request):
    Category = tbl_category.objects.all()
    data=tbl_subcategory.objects.all()
    if request.method=="POST":
        subcatname=request.POST.get('txtname')
        cat = tbl_category.objects.get(id=request.POST.get('sel_cat'))
        tbl_subcategory.objects.create(subcat_name=subcatname,category=cat)
        return redirect("WebAdmin:SubCatInsertSelect")
    else:
        return render(request,"WebAdmin/SubCategory.html",{'data':data,"catdata":Category})

def delSubCategory(request,did):
    tbl_subcategory.objects.get(id=did).delete()
    return redirect("WebAdmin:SubCatInsertSelect")

def SubCategoryupdate(request,eid):
    catdata = tbl_category.objects.all()
    editdata=tbl_subcategory.objects.get(id=eid)
    if request.method=="POST":
        editdata.subcat_name=request.POST.get("txtname")
        cat = tbl_category.objects.get(id=request.POST.get('sel_cat'))
        editdata.category = cat
        editdata.save()
        return redirect("WebAdmin:SubCatInsertSelect")
    else:
        return render(request,"WebAdmin\SubCategory.html",{"editdata":editdata,"catdata":catdata})


def ComplaintListNew(request):
    userdata=tbl_user.objects.all()
    userComplaint=tbl_complaint.objects.filter(complaint_status=0,user__in=userdata)
    return render(request,"WebAdmin/ComplaintListNew.html",{'userComplaint':userComplaint})

def ComplaintReply(request,cid):
    complaint = tbl_complaint.objects.get(id=cid)
    if request.method=="POST":
        complaint.complaint_replydate = date.today()
        complaint.complaint_reply=request.POST.get('txtreply')
        complaint.complaint_status=1
        complaint.save()
        return redirect("WebAdmin:LoadingHomePage")
    else:
        return render(request,"WebAdmin/ComplaintListReply.html",{'complaint':complaint})
    
def ComplaintSolved(request):
    userdata=tbl_user.objects.all()
    userComplaint=tbl_complaint.objects.filter(complaint_status=1,user__in=userdata)
    return render(request,"WebAdmin/ComplaintListSolved.html",{'userComplaint':userComplaint})
    

def UserFeedbackNew(request):
    data=tbl_feedback.objects.filter(feedback_status=0)
    return render(request,"WebAdmin/UserFeedBack.html",{'data':data})


#shop

def shopListNew(request):
    userdata = tbl_shop.objects.filter(shop_status=0)
    return render(request,"WebAdmin/ShopListNew.html",{"userdata":userdata})

def acceptshop(request,aid):
    user = tbl_shop.objects.get(id=aid)
    user.shop_status = 1
    user.save()
    return redirect("WebAdmin:LoadingHomePage")

def rejectshop(request,rid):
    user = tbl_shop.objects.get(id=rid)
    user.shop_status = 2
    user.save()
    return redirect("WebAdmin:LoadingHomePage")

def ShopListAccepted(request):
    userdata = tbl_shop.objects.filter(shop_status=1)
    return render(request,"WebAdmin/ShopListAccepted.html",{"userdata":userdata})

def ShopListRejected(request):
    userdata = tbl_shop.objects.filter(shop_status=2)
    return render(request,"WebAdmin/ShopListRejected.html",{"userdata":userdata})

#workshop

def workshopListNew(request):
    userdata = tbl_workshop.objects.filter(workshop_status=0)
    return render(request,"WebAdmin/WorkShopListNew.html",{"userdata":userdata})

def acceptworkshop(request,aid):
    user = tbl_workshop.objects.get(id=aid)
    user.workshop_status = 1
    user.save()
    return redirect("WebAdmin:LoadingHomePage")

def rejectworkshop(request,rid):
    user = tbl_workshop.objects.get(id=rid)
    user.workshop_status = 2
    user.save()
    return redirect("WebAdmin:LoadingHomePage")

def workShopListAccepted(request):
    userdata = tbl_workshop.objects.filter(workshop_status=1)
    return render(request,"WebAdmin/WorkShopListAccepted.html",{"userdata":userdata})

def workShopListRejected(request):
    userdata = tbl_workshop.objects.filter(workshop_status=2)
    return render(request,"WebAdmin/WorkShopListRejected.html",{"userdata":userdata})

#
def BrandInsertSelect(request):
    data=tbl_brand.objects.all()
    if request.method=="POST":
        catName=request.POST.get('txtname')
        tbl_brand.objects.create(brand_name=catName)
        return redirect("WebAdmin:BrandInsertSelect")
    else:
        return render(request,"WebAdmin/Brand.html",{'data':data})

def delBrand(request,did):
    tbl_brand.objects.get(id=did).delete()
    return redirect("WebAdmin:BrandInsertSelect")

def Brandupdate(request,eid):
    editdata=tbl_brand.objects.get(id=eid)
    if request.method=="POST":
        editdata.brand_name=request.POST.get("txtname")
        editdata.save()
        return redirect("WebAdmin:BrandInsertSelect")
    else:
        return render(request,"WebAdmin\Brand.html",{"editdata":editdata})

#
def ServiceTypeInsertSelect(request):
    data=tbl_servicetype.objects.all()
    if request.method=="POST":
        catName=request.POST.get('txtname')
        tbl_servicetype.objects.create(servicetype_name=catName)
        return redirect("WebAdmin:ServiceTypeInsertSelect")
    else:
        return render(request,"WebAdmin/ServiceType.html",{'data':data})

def delServiceType(request,did):
    tbl_servicetype.objects.get(id=did).delete()
    return redirect("WebAdmin:ServiceTypeInsertSelect")

def ServiceTypeupdate(request,eid):
    editdata=tbl_servicetype.objects.get(id=eid)
    if request.method=="POST":
        editdata.servicetype_name=request.POST.get("txtname")
        editdata.save()
        return redirect("WebAdmin:ServiceTypeInsertSelect")
    else:
        return render(request,"WebAdmin\ServiceType.html",{"editdata":editdata})

#
def BoatTypeInsertSelect(request):
    data=tbl_boattype.objects.all()
    if request.method=="POST":
        catName=request.POST.get('txtname')
        tbl_boattype.objects.create(boattype_name=catName)
        return redirect("WebAdmin:BoatTypeInsertSelect")
    else:
        return render(request,"WebAdmin/BoatType.html",{'data':data})

def delBoatType(request,did):
    tbl_boattype.objects.get(id=did).delete()
    return redirect("WebAdmin:BoatTypeInsertSelect")

def BoatTypeupdate(request,eid):
    editdata=tbl_boattype.objects.get(id=eid)
    if request.method=="POST":
        editdata.boattype_name=request.POST.get("txtname")
        editdata.save()
        return redirect("WebAdmin:BoatTypeInsertSelect")
    else:
        return render(request,"WebAdmin\BoatType.html",{"editdata":editdata})