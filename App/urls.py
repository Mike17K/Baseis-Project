from django.urls import path
from . import views

urlpatterns = [
    path("",views.index,name="index"),
    path("userLogin/",views.userLogin,name="userLogin"),
    path("userRegister/",views.userRegister,name="userRegister"),
    path("userPage/<int:AFM>/",views.userPage,name="userPage"),
    path("adminPage/",views.adminPage,name="adminPage"),
    path("message/<int:aggelia_id>/<int:uid>/",views.messagePage,name="messagePage"),
    path("refresh/",views.refreshDatabace,name="refreshDatabace")
]