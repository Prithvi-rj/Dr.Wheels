from django.urls import path
from WebUser import views

app_name="WebUser"
urlpatterns = [
    
    path('homepage/',views.homepage,name="homepage"),
    path('My_profile/',views.my_pro,name="my_pro"),
    path('editprofile/',views.editprofile,name="editprofile"),
    path('changepassword/',views.changepassword,name="changepassword"),

    path('POSTComplaint/',views.POSTComplaint,name="POSTComplaint"),
    path('delComplaint/<int:did>',views.delComplaint,name="delComplaint"),

    path('UserFeedback/', views.UserFeedback, name='UserFeedback'),
    path('delFeedback/<int:did>',views.delFeedback,name="delFeedback"),

    path('SearchServices/',views.SearchServices,name="SearchServices"),
    path('requestService/<int:did>', views.requestService,name="requestService"),
    path('requestServiceList/',views.requestServiceList,name="requestServiceList"),
    path('delRequest/<int:did>',views.delRequest,name="delRequest"),
    path('requestServiceListAccepted/',views.requestServiceListAccepted,name="requestServiceListAccepted"),
    path('requestServiceListRejected/',views.requestServiceListRejected,name="requestServiceListRejected"),
    path('requestServiceListCompleted/',views.requestServiceListCompleted,name="requestServiceListCompleted"),
    path('requestServiceListAssigned/',views.requestServiceListAssigned,name="requestServiceListAssigned"),


    path('SearchBoat/',views.SearchBoat,name="SearchBoat"),
    path('requestBoatService/<int:did>', views.requestBoatService,name="requestBoatService"),
    path('requestBoatServiceList/',views.requestBoatServiceList,name="requestBoatServiceList"),
    path('delBoatRequest/<int:did>',views.delBoatRequest,name="delBoatRequest"),
    path('requestBoatServiceListAccepted/',views.requestBoatServiceListAccepted,name="requestBoatServiceListAccepted"),
    path('requestBoatServiceListRejected/',views.requestBoatServiceListRejected,name="requestBoatServiceListRejected"),

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

    path('logout/',views.logout,name="logout"),

]