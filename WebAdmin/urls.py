from django.contrib import admin
from django.urls import path
from WebAdmin import views

app_name="WebAdmin"

urlpatterns = [
    path('admin/', admin.site.urls),

    path('HomePage/',views.LoadingHomePage,name="LoadingHomePage"),

    path('District/', views.districtInsertSelect,name="districtInsertSelect"),
    path('delDistrict/<int:did>', views.delDistrict,name="delDistrict"),
    path('districtupdate/<int:eid>',views.districtupdate,name="districtupdate"),

    path('AdminRegistration/', views.adminInsertSelect,name="adminInsertSelect"),
    path('delAdminReg/<int:did>', views.delAdminReg,name="delAdminReg"),
    path('adminRegUpdate/<int:eid>',views.adminRegUpdate,name="adminRegUpdate"),


    path('Place/', views.placeInsertSelect,name="placeInsertSelect"),
    path('delPlace/<int:did>', views.delPlace,name="delPlace"),
    path('placeupdate/<int:eid>',views.placeupdate,name="placeupdate"),

    path('UserListNew/',views.userListNew,name="userListNew"),
  

    path('Category/', views.CategoryInsertSelect,name="CategoryInsertSelect"),
    path('delCategory/<int:did>', views.delCategory,name="delCategory"),
    path('Categoryupdate/<int:eid>',views.Categoryupdate,name="Categoryupdate"),

    path('SubCategory/', views.SubCatInsertSelect,name="SubCatInsertSelect"),
    path('delSubCategory/<int:did>', views.delSubCategory,name="delSubCategory"),
    path('SubCategoryupdate/<int:eid>',views.SubCategoryupdate,name="SubCategoryupdate"),
    
 

    path('ComplaintListNew/',views.ComplaintListNew,name="ComplaintListNew"),
    path('ComplaintReply/<int:cid>',views.ComplaintReply,name="ComplaintReply"),
    path('ComplaintSolved/',views.ComplaintSolved,name="ComplaintSolved"),

    path('UserFeedbackNew/',views.UserFeedbackNew,name="UserFeedbackNew"),

    path('OwnerListNew/',views.OwnerListNew,name="OwnerListNew"),
    path('acceptowner/<int:aid>',views.acceptowner,name="acceptowner"),
    path('rejectowner/<int:rid>',views.rejectowner,name="rejectowner"),
    path('OwnerListAccepted/',views.OwnerListAccepted,name="OwnerListAccepted"),
    path('OwnerListRejected/',views.OwnerListRejected,name="OwnerListRejected"),

    path('shopListNew/',views.shopListNew,name="shopListNew"),
    path('acceptshop/<int:aid>',views.acceptshop,name="acceptshop"),
    path('rejectshop/<int:rid>',views.rejectshop,name="rejectshop"),
    path('ShopListAccepted/',views.ShopListAccepted,name="ShopListAccepted"),
    path('ShopListRejected/',views.ShopListRejected,name="ShopListRejected"),


    path('workshopListNew/',views.workshopListNew,name="workshopListNew"),
    path('acceptworkshop/<int:aid>',views.acceptworkshop,name="acceptworkshop"),
    path('rejectworkshop/<int:rid>',views.rejectworkshop,name="rejectworkshop"),
    path('workShopListAccepted/',views.workShopListAccepted,name="workShopListAccepted"),
    path('workShopListRejected/',views.workShopListRejected,name="workShopListRejected"),

    path('Brand/', views.BrandInsertSelect,name="BrandInsertSelect"),
    path('delBrand/<int:did>', views.delBrand,name="delBrand"),
    path('Brandupdate/<int:eid>',views.Brandupdate,name="Brandupdate"),

    path('ServiceType/', views.ServiceTypeInsertSelect,name="ServiceTypeInsertSelect"),
    path('delServiceType/<int:did>', views.delServiceType,name="delServiceType"),
    path('ServiceTypeupdate/<int:eid>',views.ServiceTypeupdate,name="ServiceTypeupdate"),

    path('BoatType/', views.BoatTypeInsertSelect,name="BoatTypeInsertSelect"),
    path('delBoatType/<int:did>', views.delBoatType,name="delBoatType"),
    path('BoatTypeupdate/<int:eid>',views.BoatTypeupdate,name="BoatTypeupdate"),
]