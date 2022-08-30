from django.urls import path, include
from . import views

# URL Config
urlpatterns = [

    # login
    path("accounts/", include("django.contrib.auth.urls")),
    path("register",views.register_request, name="register"),
    path("login", views.login_request, name="login"),
    path("tickets",views.ticket,name='tickets'),
    path("profile/",views.view_profile,name='profile'),
    path("profile/edit",views.edit_profile,name='edit_profile'),
    path('home/', views.homeview,name='home'),
    path("table/",views.tickettable,name= "table")
]