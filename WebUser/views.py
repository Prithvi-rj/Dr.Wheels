from django.shortcuts import render,redirect
from WebGuest.models import *
from WebUser.models import *
from WebWorkShop.models import *
from WebShop.models import *
# Create your views here.

def homepage(request):
    return render(request,"WebUser/HomePage.html")

def logout(request):
    del request.session["uid"]
    return redirect("WebGuest:Login")

def my_pro(request):
    data=tbl_user.objects.get(id=request.session["uid"])
    return render(request,"WebUser/MyProfile.html",{'data':data})

def editprofile(request):
    prodata=tbl_user.objects.get(id=request.session["uid"])
    if request.method=="POST":
        prodata.user_name=request.POST.get('txtname')
        prodata.user_contact=request.POST.get('txtcon')
        prodata.user_email=request.POST.get('txtemail')
        prodata.save()
        return render(request,"WebUser/EditProfile.html",{'msg':"Profile Updated"})
    else:
        return render(request,"WebUser/EditProfile.html",{'prodata':prodata})

def changepassword(request):
    if request.method=="POST":
        ccount=tbl_user.objects.filter(id=request.session["uid"],user_password=request.POST.get('txtcurpass')).count()
        if ccount>0:
            if request.POST.get('txtnewpass')==request.POST.get('txtconpass'):
                userdata=tbl_user.objects.get(id=request.session["uid"],user_password=request.POST.get('txtcurpass'))
                userdata.user_password=request.POST.get('txtnewpass')
                userdata.save()
                return render(request,"WebUser/ChangePassword.html",{'msg':"Password Updated"})
            else:
                return render(request,"WebUser/ChangePassword.html",{'msg1':"Error in confirm Password"})
        else:
            return render(request,"WebUser/ChangePassword.html",{'msg1':"Error in current password"})
    else:
        return render(request,"WebUser/ChangePassword.html")

def POSTComplaint(request):
    data=tbl_complaint.objects.filter(user=request.session["uid"])
    userID=tbl_user.objects.get(id=request.session["uid"])
    if request.method=="POST":
        title=request.POST.get('txttitle')
        details=request.POST.get('txtcomplaint')
        tbl_complaint.objects.create(complaint_title=title,complaint_details=details,user=userID)
        return redirect("WebUser:POSTComplaint")
    else:
        return render(request,"WebUser/POSTComplaint.html",{"data":data})
    
def delComplaint(request,did):
    tbl_complaint.objects.get(id=did).delete()
    return redirect("User:POSTComplaint")


def UserFeedback(request):
    data=tbl_feedback.objects.filter(user=request.session["uid"])
    userID=tbl_user.objects.get(id=request.session["uid"])
    if request.method=="POST":
        subject=request.POST.get('txtsubject')
        details=request.POST.get('txtfeedback')
        tbl_feedback.objects.create(feedback_subject=subject,feedback_details=details,user=userID)
        return redirect("WebUser:UserFeedback")
    else:
        return render(request,"WebUser/UserFeedback.html",{"data":data})
   

def delFeedback(request,did):
    tbl_feedback.objects.get(id=did).delete()
    return redirect("WebUser:UserFeedback")

#
def SearchServices(request):
    category = tbl_servicetype.objects.all()
    data = tbl_service.objects.all()
    if request.method=="POST":
        category = tbl_servicetype.objects.get(id=request.POST.get('sel_type'))
        data = tbl_service.objects.filter(servicetype=category)
        return render(request,"WebUser/SearchServices.html",{"data":data})
    else:
        return render(request,"WebUser/SearchServices.html",{"category":category,"data":data})


def requestService(request,did):
    editdata=tbl_service.objects.get(id=did)
    userID=tbl_user.objects.get(id=request.session["uid"])
    if request.method=="POST":
        tbl_requestservice.objects.create(user=userID,request_message=request.POST.get("txtmsg"),service=editdata)
        return redirect("WebUser:homepage")
    else:
        return render(request,"WebUser\BookServicesNow.html",{"userdata":editdata})


def requestServiceList(request):
    userID=tbl_user.objects.get(id=request.session["uid"])
    data = tbl_requestservice.objects.filter(request_status='0',user=userID)
    return render(request,"WebUser/ServiceListRequested.html",{"data":data})

def delRequest(request,did):
    tbl_requestservice.objects.get(id=did).delete()
    return redirect("WebUser:homepage")

def requestServiceListAccepted(request):
    userID=tbl_user.objects.get(id=request.session["uid"])
    data = tbl_requestservice.objects.filter(request_status='1',user=userID)
    return render(request,"WebUser/ServiceListAccepted.html",{"data":data})

def requestServiceListRejected(request):
    userID=tbl_user.objects.get(id=request.session["uid"])
    data = tbl_requestservice.objects.filter(request_status='2',user=userID)
    return render(request,"WebUser/ServiceListRejected.html",{"data":data})

def requestServiceListAssigned(request):
    userID=tbl_user.objects.get(id=request.session["uid"])
    data = tbl_requestservice.objects.filter(request_status='4',user=userID)
    return render(request,"WebUser/ServiceListAssigned.html",{"data":data})


def requestServiceListCompleted(request):
    userID=tbl_user.objects.get(id=request.session["uid"])
    data = tbl_requestservice.objects.filter(request_status='3',user=userID)
    return render(request,"WebUser/ServiceListComplete.html",{"data":data})


#
def SearchBoat(request):
    category = tbl_boattype.objects.all()
    data = tbl_boatdetails.objects.all()
    if request.method=="POST":
        category = tbl_boattype.objects.get(id=request.POST.get('sel_type'))
        data = tbl_boatdetails.objects.filter(boattype=category)
        return render(request,"WebUser/SearchBoat.html",{"data":data})
    else:
        return render(request,"WebUser/SearchBoat.html",{"category":category,"data":data})


def requestBoatService(request,did):
    editdata=tbl_boatdetails.objects.get(id=did)
    userID=tbl_user.objects.get(id=request.session["uid"])
    if request.method=="POST":
        boatid = tbl_boatdetails.objects.get(id=did)
        tbl_requestboat.objects.create(user=userID,request_todate=request.POST.get("txtdate"),request_message=request.POST.get("txtmsg"),boat=boatid)
        return redirect("WebUser:homepage")
    else:
        return render(request,"WebUser\BookBoatNow.html",{"userdata":editdata})


def requestBoatServiceList(request):
    userID=tbl_user.objects.get(id=request.session["uid"])
    data = tbl_requestboat.objects.filter(request_status='0',user=userID)
    return render(request,"WebUser/BoatServiceRequested.html",{"data":data})

def delBoatRequest(request,did):
    tbl_requestboat.objects.get(id=did).delete()
    return redirect("WebUser:homepage")

def requestBoatServiceListAccepted(request):
    userID=tbl_user.objects.get(id=request.session["uid"])
    data = tbl_requestboat.objects.filter(request_status='1',user=userID)
    return render(request,"WebUser/BoatServiceAccepted.html",{"data":data})

def requestBoatServiceListRejected(request):
    userID=tbl_user.objects.get(id=request.session["uid"])
    data = tbl_requestboat.objects.filter(request_status='2',user=userID)
    return render(request,"WebUser/BoatServiceRejected.html",{"data":data})

def viewproduct(request):
    pdt = tbl_product.objects.all()
    return render(request,"WebUser/View_product.html",{"product":pdt})

def Addcart(request,pid):
    productdata=tbl_product.objects.get(id=pid)
    custdata=tbl_user.objects.get(id=request.session["uid"])
    bookingcount=tbl_booking.objects.filter(user=custdata,booking_status=0).count()
    if bookingcount>0:
        bookingdata=tbl_booking.objects.get(user=custdata,booking_status=0)
        cartcount=tbl_cart.objects.filter(booking=bookingdata,product=productdata).count()
        if cartcount>0:
            msg="Already added"
            return render(request,"WebUser/View_product.html",{'msg':msg})
        else:
            tbl_cart.objects.create(booking=bookingdata,product=productdata)
            return redirect("WebUser:viewproduct")
    else:
        tbl_booking.objects.create(user=custdata)
        bookingcount=tbl_booking.objects.filter(booking_status=0,user=custdata).count()
        if bookingcount>0:
            bookingdata=tbl_booking.objects.get(user=custdata,booking_status=0)
            cartcount=tbl_cart.objects.filter(booking=bookingdata,product=productdata).count()
            if cartcount>0:
                msg="Already added"
                return render(request,"WebUser/View_product.html",{'msg':msg})
            else:
                tbl_cart.objects.create(booking=bookingdata,product=productdata)
                return redirect("WebUser:viewproduct")

def Mycart(request):
    if request.method=="POST":
        bookingdata=tbl_booking.objects.get(id=request.session["bookingid"])
        bookingdata.booking_amount=request.POST.get("carttotalamt")
        bookingdata.booking_status=1
        bookingdata.save()
        return redirect("WebUser:payment")
    else:
        customerdata=tbl_user.objects.get(id=request.session["uid"])
        bcount=tbl_booking.objects.filter(user=customerdata,booking_status=0).count()
        #cartcount=cart.objects.filter(booking__customer=customerdata,booking__status=0).count()
        if bcount>0:
            #cartdata=cart.objects.filter(booking__customer=customerdata,booking__status=0)
            book=tbl_booking.objects.get(user=customerdata,booking_status=0)
            bid=book.id
            request.session["bookingid"]=bid
            bkid=tbl_booking.objects.get(id=bid)
            cartdata=tbl_cart.objects.filter(booking=bkid)
            return render(request,"WebUser/MyCart.html",{'data':cartdata})
        else:
            return render(request,"WebUser/MyCart.html")

def DelCart(request,did):
    tbl_cart.objects.get(id=did).delete()
    return redirect("WebUser:Mycart")

def CartQty(request):
    qty=request.GET.get('QTY')
    cartid=request.GET.get('ALT')
    cartdata=tbl_cart.objects.get(id=cartid)
    cartdata.cart_qty=qty
    cartdata.save()
    return redirect("WebUser:Mycart")

def payment(request):
    booking = tbl_booking.objects.get(id=request.session["bookingid"])
    if request.method == "POST":
        booking.booking_status = 2
        booking.save()
        return redirect("WebUser:loader")
    else:
        return render(request,"WebUser/Payment.html",{"total":booking})

def loader(request):
    return render(request,"WebUser/Loader.html")

def paymentsuc(request):
    return render(request,"WebUser/Payment_suc.html")

def mybooking(request):
    bk  = tbl_booking.objects.filter(booking_status=2,user=request.session["uid"])
    return render(request,"WebUser/MyBooking.html",{"booking":bk})

def myproduct(request,id):
    bk  = tbl_cart.objects.filter(booking=id)
    return render(request,"WebUser/MyProduct.html",{"booking":bk})