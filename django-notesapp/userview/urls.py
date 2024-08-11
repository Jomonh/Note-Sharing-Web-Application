from os import name
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name="home"),
    path('login/',views.login_view,name="login"),
    path('register/',views.register_view,name="register"),
    path('logged/',views.logged_view,name="logged"),
    path('logout/',views.logout_view,name="logout"),
    path('semone/',views.semone_view,name="semone"),
    path('semtwo/',views.semtwo_view,name="semtwo"),
    path('semthree/',views.semthree_view,name="semthree"),
    path('semfour/',views.semfour_view,name="semfour"),
    path('admincontrol/',views.admin_view,name="adminview"),

    path('profile/',views.profile_view,name="profile"),
    path('profile/deleteprofile/',views.delete_profile,name="deleteprofile")
]