from django.urls import path, include
from . import views

# URL Config
urlpatterns = [

    # login
    path("accounts/", include("django.contrib.auth.urls")),
    path("register",views.register_request, name="register"),
    path("login", views.login_request, name="login"),
    path("tickets",views.ticket,name='tickets')
]