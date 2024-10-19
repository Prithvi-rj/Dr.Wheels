from django.urls import path
from WebWorkShop import views

app_name="WebWorkShop"
urlpatterns = [
    
    path('homepage/',views.homepage,name="homepage"),
    path('My_profile/',views.my_pro,name="my_pro"),
    path('editprofile/',views.editprofile,name="editprofile"),
    path('changepassword/',views.changepassword,name="changepassword"),

    path('ServiceDetails/',views.ServiceDetails,name="ServiceDetails"),
    path('deleteServiceDetails/<int:did>',views.deleteServiceDetails,name="deleteServiceDetails"),

    path('requestServiceList/',views.requestServiceList,name="requestServiceList"),
    path('acceptrequest/<int:aid>',views.acceptrequest,name="acceptrequest"),
    path('rejectrequest/<int:rid>',views.rejectrequest,name="rejectrequest"),
    path('completerequest/<int:rid>',views.completerequest,name="completerequest"),
    path('AssignNowRequest/<int:asid>',views.AssignNowRequest,name="AssignNowRequest"),
    path('requestServiceListAccepted/',views.requestServiceListAccepted,name="requestServiceListAccepted"),
    path('requestServiceListAssigned/',views.requestServiceListAssigned,name="requestServiceListAssigned"),
    path('requestServiceListRejected/',views.requestServiceListRejected,name="requestServiceListRejected"),
    path('requestServiceListCompleted/',views.requestServiceListCompleted,name="requestServiceListCompleted"),

    path('NewMechanic/',views.NewMechanic,name="NewMechanic"),
    path('AjaxPlace/',views.ajaxplace,name="ajaxplace"),
    path('MechaniList/',views.MechaniList,name="MechaniList"),
    path('acceptmechanic/<int:aid>',views.acceptmechanic,name="acceptmechanic"),
    path('rejectmechanic/<int:rid>',views.rejectmechanic,name="rejectmechanic"),
    path('MechanicListAccepted/',views.MechanicListAccepted,name="MechanicListAccepted"),
    path('MechanicListRejected/',views.MechanicListRejected,name="MechanicListRejected"),



    path('logout/',views.logout,name="logout"),

]