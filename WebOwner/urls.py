from django.urls import path
from WebOwner import views

app_name="WebOwner"
urlpatterns = [
    
    path('homepage/',views.homepage,name="homepage"),
    path('My_profile/',views.my_pro,name="my_pro"),
    path('editprofile/',views.editprofile,name="editprofile"),
    path('changepassword/',views.changepassword,name="changepassword"),

    path('BoatDetails/',views.BoatDetails,name="BoatDetails"),
    path('deleteBoatDetails/<int:did>',views.deleteBoatDetails,name="deleteBoatDetails"),

    path('requestServiceList/',views.requestServiceList,name="requestServiceList"),
    path('acceptrequest/<int:aid>',views.acceptrequest,name="acceptrequest"),
    path('rejectrequest/<int:rid>',views.rejectrequest,name="rejectrequest"),
    path('requestServiceListAccepted/',views.requestServiceListAccepted,name="requestServiceListAccepted"),
    path('requestServiceListRejected/',views.requestServiceListRejected,name="requestServiceListRejected"),
  
    

    path('viewproduct/',views.viewproduct,name="viewproduct"),

    path('Addcart/<int:pid>',views.Addcart,name="Addcart"),
    path('Mycart/',views.Mycart,name="Mycart"),
    path('DelCart/<int:did>',views.DelCart,name="DelCart"),
    path('CartQty/',views.CartQty,name="CartQty"),

    path('payment/',views.payment,name="payment"),
    path('loader/',views.loader,name="loader"),
    path('paymentsuc/',views.paymentsuc,name="paymentsuc"),

    path('mybooking/',views.mybooking,name="mybooking"),
    path('myproduct/<int:id>',views.myproduct,name="myproduct"),


    path('SearchServices/',views.SearchServices,name="SearchServices"),
    path('requestService/<int:did>', views.requestService,name="requestService"),
    path('requestServiceListOwner/',views.requestServiceListOwner,name="requestServiceListOwner"),
    path('delRequest/<int:did>',views.delRequest,name="delRequest"),
    path('requestServiceListAcceptedOwner/',views.requestServiceListAcceptedOwner,name="requestServiceListAcceptedOwner"),
    path('requestServiceListRejectedOwner/',views.requestServiceListRejectedOwner,name="requestServiceListRejectedOwner"),
    path('requestServiceListCompletedOwner/',views.requestServiceListCompletedOwner,name="requestServiceListCompletedOwner"),

    path('logout/',views.logout,name="logout"),

]