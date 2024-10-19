from django.shortcuts import render,redirect
from WebGuest.models import *
from WebOwner.models import *
from WebAdmin.models import *
from WebUser.models import *
from django.db.models import Sum
# Create your views here.

def homepage(request):
    return render(request,"WebOwner/HomePage.html")

def logout(request):
    del request.session["oid"]
    return redirect("WebGuest:Login")

def my_pro(request):
    data=tbl_boatowner.objects.get(id=request.session["oid"])
    return render(request,"WebOwner/MyProfile.html",{'data':data})

def editprofile(request):
    prodata=tbl_boatowner.objects.get(id=request.session["oid"])
    if request.method=="POST":
        prodata.owner_name=request.POST.get('txtname')
        prodata.owner_contact=request.POST.get('txtcon')
        prodata.owner_email=request.POST.get('txtemail')
        prodata.save()
        return render(request,"WebOwner/EditProfile.html",{'msg':"Profile Updated"})
    else:
        return render(request,"WebOwner/EditProfile.html",{'prodata':prodata})

def changepassword(request):
    if request.method=="POST":
        ccount=tbl_boatowner.objects.filter(id=request.session["oid"],owner_password=request.POST.get('txtcurpass')).count()
        if ccount>0:
            if request.POST.get('txtnewpass')==request.POST.get('txtconpass'):
                userdata=tbl_boatowner.objects.get(id=request.session["oid"],owner_password=request.POST.get('txtcurpass'))
                userdata.owner_password=request.POST.get('txtnewpass')
                userdata.save()
                return render(request,"WebOwner/ChangePassword.html",{'msg':"Password Updated"})
            else:
                return render(request,"WebOwner/ChangePassword.html",{'msg1':"Error in confirm Password"})
        else:
            return render(request,"WebOwner/ChangePassword.html",{'msg1':"Error in current password"})
    else:
        return render(request,"WebOwner/ChangePassword.html")



#
def BoatDetails(request):
    category = tbl_boattype.objects.all()
    prodata=tbl_boatowner.objects.get(id=request.session["oid"])
    data = tbl_boatdetails.objects.filter(owner=prodata)
    if request.method=="POST":
        prodata=tbl_boatowner.objects.get(id=request.session["oid"])
        category = tbl_boattype.objects.get(id=request.POST.get('sel_type'))
        tbl_boatdetails.objects.create(boat_photo=request.FILES.get("fileImage"),boat_proof=request.FILES.get("fileProof"),boat_capacity=request.POST.get("txtcapacity"),boat_details=request.POST.get("txtdetails"),boat_name=request.POST.get("txtname"),boat_rate=request.POST.get("txtscale"),boattype=category,owner=prodata)
        return redirect("WebOwner:BoatDetails")
    else:
        return render(request,"WebOwner/BoatDetails.html",{"category":category,"data":data})


def deleteBoatDetails(request,did):
    tbl_boatdetails.objects.get(id=did).delete()
    return redirect("WebOwner:BoatDetails")

#
def requestServiceList(request):
    provider=tbl_boatowner.objects.get(id=request.session["oid"])
    userdata = tbl_requestboat.objects.filter(request_status=0,boat__owner=provider)
    # print(userdata)
    return render(request,"WebOwner/BoatServiceRequested.html",{"userdata":userdata})

def acceptrequest(request,aid):
    user = tbl_requestboat.objects.get(id=aid)
    user.request_status = 1
    user.save()
    return redirect("WebOwner:homepage")

def rejectrequest(request,rid):
    user = tbl_requestboat.objects.get(id=rid)
    user.request_status = 2
    user.save()
    return redirect("WebOwner:homepage")

def requestServiceListAccepted(request):
    provider=tbl_boatowner.objects.get(id=request.session["oid"])
    userdata = tbl_requestboat.objects.filter(request_status=1,boat__owner=provider)
    return render(request,"WebOwner/BoatServiceAccepted.html",{"userdata":userdata})

def requestServiceListRejected(request):
    provider=tbl_boatowner.objects.get(id=request.session["oid"])
    userdata = tbl_requestboat.objects.filter(request_status=2,boat__owner=provider)
    return render(request,"WebOwner/BoatServiceRejected.html",{"userdata":userdata})


#
def SearchServices(request):
    category = tbl_servicetype.objects.all()
    data = tbl_service.objects.all()
    if request.method=="POST":
        category = tbl_servicetype.objects.get(id=request.POST.get('sel_type'))
        data = tbl_service.objects.filter(servicetype=category)
        return render(request,"WebOwner/SearchServices.html",{"data":data})
    else:
        return render(request,"WebOwner/SearchServices.html",{"category":category,"data":data})


def requestService(request,did):
    editdata=tbl_service.objects.get(id=did)
    userID=tbl_boatowner.objects.get(id=request.session["oid"])
    if request.method=="POST":
        tbl_requestserviceowner.objects.create(owner=userID,request_message=request.POST.get("txtmsg"),service=editdata)
        return redirect("WebOwner:homepage")
    else:
        return render(request,"WebOwner\BookServicesNow.html",{"userdata":editdata})


def requestServiceListOwner(request):
    userID=tbl_boatowner.objects.get(id=request.session["oid"])
    data = tbl_requestserviceowner.objects.filter(request_status='0',owner=userID)
    return render(request,"WebOwner/ServiceListRequested.html",{"data":data})

def delRequest(request,did):
    tbl_requestserviceowner.objects.get(id=did).delete()
    return redirect("WebOwner:homepage")

def requestServiceListAcceptedOwner(request):
    userID=tbl_boatowner.objects.get(id=request.session["oid"])
    data = tbl_requestserviceowner.objects.filter(request_status='1',owner=userID)
    return render(request,"WebOwner/ServiceListAccepted.html",{"data":data})

def requestServiceListRejectedOwner(request):
    userID=tbl_boatowner.objects.get(id=request.session["oid"])
    data = tbl_requestserviceowner.objects.filter(request_status='2',owner=userID)
    return render(request,"WebOwner/ServiceListRejected.html",{"data":data})


def requestServiceListCompletedOwner(request):
    userID=tbl_boatowner.objects.get(id=request.session["oid"])
    data = tbl_requestserviceowner.objects.filter(request_status='3',owner=userID)
    return render(request,"WebOwner/ServiceListCompleted.html",{"data":data})

#



def viewproduct(request):
    pdt = tbl_product.objects.all()
    return render(request,"WebOwner/View_product.html",{"product":pdt})

def Addcart(request,pid):
    productdata=tbl_product.objects.get(id=pid)
    custdata=tbl_boatowner.objects.get(id=request.session["oid"])
    bookingcount=tbl_booking.objects.filter(owner=custdata,booking_status=0).count()
    if bookingcount>0:
        bookingdata=tbl_booking.objects.get(owner=custdata,booking_status=0)
        cartcount=tbl_cart.objects.filter(booking=bookingdata,product=productdata).count()
        if cartcount>0:
            msg="Already added"
            return render(request,"WebOwner/View_product.html",{'msg':msg})
        else:
            tbl_cart.objects.create(booking=bookingdata,product=productdata)
            return redirect("WebOwner:viewproduct")
    else:
        tbl_booking.objects.create(owner=custdata)
        bookingcount=tbl_booking.objects.filter(booking_status=0,owner=custdata).count()
        if bookingcount>0:
            bookingdata=tbl_booking.objects.get(owner=custdata,booking_status=0)
            cartcount=tbl_cart.objects.filter(booking=bookingdata,product=productdata).count()
            if cartcount>0:
                msg="Already added"
                return render(request,"WebOwner/View_product.html",{'msg':msg})
            else:
                tbl_cart.objects.create(booking=bookingdata,product=productdata)
                return redirect("WebOwner:viewproduct")

def Mycart(request):
    if request.method=="POST":
        bookingdata=tbl_booking.objects.get(id=request.session["bookingid"])
        bookingdata.booking_amount=request.POST.get("carttotalamt")
        bookingdata.booking_status=1
        bookingdata.save()
        return redirect("WebOwner:payment")
    else:
        customerdata=tbl_boatowner.objects.get(id=request.session["oid"])
        bcount=tbl_booking.objects.filter(owner=customerdata,booking_status=0).count()
        #cartcount=cart.objects.filter(booking__customer=customerdata,booking__status=0).count()
        if bcount>0:
            #cartdata=cart.objects.filter(booking__customer=customerdata,booking__status=0)
            book=tbl_booking.objects.get(owner=customerdata,booking_status=0)
            bid=book.id
            request.session["bookingid"]=bid
            bkid=tbl_booking.objects.get(id=bid)
            cartdata = tbl_cart.objects.filter(booking=bkid)
            for data in cartdata:
                productid = data.product.id
                
                # Calculate the total stock and cart quantities
                pstock_qty_sum = tbl_productstock.objects.filter(product=productid).aggregate(Sum('stock_qty'))
                pstock = pstock_qty_sum['stock_qty__sum'] if pstock_qty_sum['stock_qty__sum'] is not None else 0

                cstock_qty_sum = tbl_cart.objects.filter(product=productid, booking__booking_status=1).aggregate(Sum('cart_qty'))
                cstock = cstock_qty_sum['cart_qty__sum'] if cstock_qty_sum['cart_qty__sum'] is not None else 0

                total = pstock - cstock
                
                # Add the 'total' key to the data dictionary
                data.total = total  # Assuming 'total' is a field in tbl_cart model

            
            return render(request,"WebOwner/MyCart.html",{'data':cartdata})
        else:
            return render(request,"WebOwner/MyCart.html")

def DelCart(request,did):
    tbl_cart.objects.get(id=did).delete()
    return redirect("WebOwner:Mycart")

def CartQty(request):
    qty=request.GET.get('QTY')
    cartid=request.GET.get('ALT')
    
    cartdata=tbl_cart.objects.get(id=cartid)
    cartdata.cart_qty=qty
    cartdata.save()
    return redirect("WebOwner:Mycart")

def payment(request):
    booking = tbl_booking.objects.get(id=request.session["bookingid"])
    if request.method == "POST":
        booking.booking_status = 2
        booking.save()
        return redirect("WebOwner:loader")
    else:
        return render(request,"WebOwner/Payment.html",{"total":booking})

def loader(request):
    return render(request,"WebOwner/Loader.html")

def paymentsuc(request):
    return render(request,"WebOwner/Payment_suc.html")

def mybooking(request):
    bk  = tbl_booking.objects.filter(booking_status=2,owner=request.session["oid"])
    return render(request,"WebOwner/MyBooking.html",{"booking":bk})

def myproduct(request,id):
    bk  = tbl_cart.objects.filter(booking=id)
    return render(request,"WebOwner/MyProduct.html",{"booking":bk})