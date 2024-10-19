from django.urls import path
from Mechanic import views

app_name="Mechanic"
urlpatterns = [
    
    path('homepage/',views.homepage,name="homepage"),
    path('My_profile/',views.my_pro,name="my_pro"),
    path('editprofile/',views.editprofile,name="editprofile"),
    path('changepassword/',views.changepassword,name="changepassword"),

    
    path('requestServiceListAssigned/',views.requestServiceListAssigned,name="requestServiceListAssigned"),
    path('completerequest/<int:rid>',views.completerequest,name="completerequest"),
    path('requestServiceListCompleted/',views.requestServiceListCompleted,name="requestServiceListCompleted"),





    path('logout/',views.logout,name="logout"),

]