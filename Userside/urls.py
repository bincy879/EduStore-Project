from django.urls import path
from Userside import views
urlpatterns=[
    path('home/',views.home,name="home"),
    path('about/',views.about,name="about"),
    path('products/',views.products,name="products"),
    path('disPdt/<itemCatg>/',views.disPdt,name="disPdt"),
    path('show_pdt/<int:dataid>/',views.show_pdt,name="show_pdt"),
    path('reg/',views.reg,name="reg"),
    path('log/',views.login,name="log"),
    path('reg_save/',views.reg_save,name="reg_save"),
    path('log_save/',views.log_save,name="log_save"),
    path('logout/',views.logout,name="logout"),
    path('contact/',views.contact,name="contact"),
    path('msg_save/',views.msg_save,name="msg_save"),

]