from django.shortcuts import render,redirect
from WebGuest.models import *
from WebShop.models import *
from WebUser.models import *
# Create your views here.

def homepage(request):
    return render(request,"WebShop/HomePage.html")

def logout(request):
    del request.session["sid"]
    return redirect("WebGuest:Login")

def my_pro(request):
    data=tbl_shop.objects.get(id=request.session["sid"])
    return render(request,"WebShop/MyProfile.html",{'data':data})

def editprofile(request):
    prodata=tbl_shop.objects.get(id=request.session["sid"])
    if request.method=="POST":
        prodata.shop_name=request.POST.get('txtname')
        prodata.shop_contact=request.POST.get('txtcon')
        prodata.shop_email=request.POST.get('txtemail')
        prodata.save()
        return render(request,"WebShop/EditProfile.html",{'msg':"Profile Updated"})
    else:
        return render(request,"WebShop/EditProfile.html",{'prodata':prodata})

def changepassword(request):
    if request.method=="POST":
        ccount=tbl_shop.objects.filter(id=request.session["sid"],shop_password=request.POST.get('txtcurpass')).count()
        if ccount>0:
            if request.POST.get('txtnewpass')==request.POST.get('txtconpass'):
                userdata=tbl_shop.objects.get(id=request.session["sid"],shop_password=request.POST.get('txtcurpass'))
                userdata.shop_password=request.POST.get('txtnewpass')
                userdata.save()
                return render(request,"WebShop/ChangePassword.html",{'msg':"Password Updated"})
            else:
                return render(request,"WebShop/ChangePassword.html",{'msg1':"Error in confirm Password"})
        else:
            return render(request,"WebShop/ChangePassword.html",{'msg1':"Error in current password"})
    else:
        return render(request,"WebShop/ChangePassword.html")


def productRegistration(request):
    category = tbl_category.objects.all()
    brand = tbl_brand.objects.all()
    prodata=tbl_shop.objects.get(id=request.session["sid"])
    data=tbl_product.objects.filter(shop=prodata)
    if request.method=="POST":
        subcat = tbl_subcategory.objects.get(id=request.POST.get('sel_subcat'))
        brand = tbl_brand.objects.get(id=request.POST.get('sel_brand'))
        shop=tbl_shop.objects.get(id=request.session["sid"])
        tbl_product.objects.create(product_name=request.POST.get("txtname"),product_details=request.POST.get("txtabout"),product_rate=request.POST.get("txtprice"),product_photo=request.FILES.get("fileImage"),subcat=subcat,brand=brand,shop=shop)
        return redirect("WebShop:productRegistration")
    else:
        return render(request,"WebShop/ProductDetails.html",{"category":category,"brand":brand,"datat":data})

def ajaxsubcategory(request):
    dis = tbl_category.objects.get(id=request.GET.get("did"))
    subcat = tbl_subcategory.objects.filter(category=dis)
    return render(request,"WebShop/AjaxSubcategory.html",{"placedata":subcat})

def delProduct(request,did):
    tbl_product.objects.get(id=did).delete()
    return redirect("WebShop:productRegistration")
    
def addstock(request,id):
    pdt = tbl_product.objects.get(id=id)
    data=tbl_productstock.objects.filter(product=pdt)
    if request.method == "POST":
        #oldstock = pdt.product_stock
        #newstock = request.POST.get("txt_stock")
        #tot = int(oldstock) + int(newstock)
        #pdt.product_stock = tot
        #pdt.save()
        newstock = request.POST.get("txt_stock")
        tbl_productstock.objects.create(product=pdt,stock_qty=newstock)
        return redirect("WebShop:productRegistration")
    else:
        return render(request,"WebShop/Add_stock.html",{"data":data})

def delStock(request,did):
    tbl_productstock.objects.get(id=did).delete()
    return redirect("WebShop:productRegistration")

#
def mybooking(request):
    bk  = tbl_booking.objects.filter(booking_status=2,user=request.session["uid"])
    return render(request,"WebShop/MyBooking.html",{"booking":bk})

def myproduct(request,id):
    bk  = tbl_cart.objects.filter(booking=id)
    return render(request,"WebShop/MyProduct.html",{"booking":bk})
#

def viewbooking(request):
      shopID=tbl_shop.objects.get(id=request.session['sid'])
      booking=tbl_cart.objects.filter(product__shop=shopID)
      bk_id = []
      for i in booking:
        bk_id.append(i.booking_id)
    #   print(bk_id)
      book = tbl_booking.objects.filter(id__in=bk_id,booking_status='2')
      return render(request,"WebShop/Viewbooking.html",{'data':book})


def viewproduct(request,id):
     cart = tbl_cart.objects.filter(booking=id)
     return render(request,"WebShop/View_product.html",{"data":cart})


def orderPlacedURL(request,aid):
    user = tbl_booking.objects.get(id=aid)
    user.booking_status = 3
    user.save()
    return redirect("WebShop:homepage")


def PlacedOrder(request):
      shopID=tbl_shop.objects.get(id=request.session['sid'])
      booking=tbl_cart.objects.filter(product__shop=shopID)
      bk_id = []
      for i in booking:
        bk_id.append(i.booking_id)
    #   print(bk_id)
      book = tbl_booking.objects.filter(id__in=bk_id,booking_status='3')
      return render(request,"WebShop/PlacedOrder.html",{'data':book})
