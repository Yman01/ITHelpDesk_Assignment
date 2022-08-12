from django.urls import path, include
from . import views

# URL Config
urlpatterns = [

    # login
    path('',views.loginpage, name='login'),
    path("accounts/", include("django.contrib.auth.urls")),
]