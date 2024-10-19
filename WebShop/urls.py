from django.urls import path
from WebShop import views

app_name="WebShop"
urlpatterns = [
    
    path('homepage/',views.homepage,name="homepage"),
    path('My_profile/',views.my_pro,name="my_pro"),
    path('editprofile/',views.editprofile,name="editprofile"),
    path('changepassword/',views.changepassword,name="changepassword"),

    path('productRegistration/',views.productRegistration,name="productRegistration"),
    path('ajaxsubcategory/',views.ajaxsubcategory,name="ajaxsubcategory"),
     path('delProduct/<int:did>', views.delProduct,name="delProduct"),

    path('addstock/<int:id>',views.addstock,name="addstock"),
    path('delStock/<int:did>',views.delStock,name="delStock"),

    #path('mybooking/',views.mybooking,name="mybooking"),
    #path('myproduct/<int:id>',views.myproduct,name="myproduct"),

    path('viewbooking/',views.viewbooking,name="viewbooking"),
    path('viewproduct/<int:id>',views.viewproduct,name="viewproduct"),

    path('orderPlacedURL/<int:aid>',views.orderPlacedURL,name="orderPlacedURL"),

    path('PlacedOrder/',views.PlacedOrder,name="PlacedOrder"),





    path('logout/',views.logout,name="logout"),

]