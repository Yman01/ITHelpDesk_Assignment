from django.urls import path
from . import views

# URL Config
urlpatterns = [
    path('loginpage/', views.loginpage),
    path('signup/',views.signuppage)
]