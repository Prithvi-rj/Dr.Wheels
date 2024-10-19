from django.urls import path
from WebGuest import views
app_name="WebGuest"
urlpatterns = [

    path('NewUser/',views.userRegistration,name="userRegistration"),
    path('ownerRegistration/',views.ownerRegistration,name="ownerRegistration"),
    path('shopRegistration/',views.shopRegistration,name="shopRegistration"),
    path('workshopRegistration/',views.workshopRegistration,name="workshopRegistration"),


    path('AjaxPlace/',views.ajaxplace,name="ajaxplace"),
    path('Login/',views.Login,name="Login"),
    
    path('',views.index,name="index"),
]