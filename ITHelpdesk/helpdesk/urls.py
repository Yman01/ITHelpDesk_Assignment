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
    path('', views.homeview,name='home'),
    path('update/<int:id>', views.updateticket, name='update'),
    path('update/updaterecord/<int:id>', views.updaterecord, name='updaterecord'),
    path('delete/<int:id>', views.delete, name='delete'),
    path('profile/<int:id>', views.updateprofile, name='update'),
    path('profile/edit/updateprofilerecord/<int:id>', views.updateprofilerecord, name='updateprofilerecord'),
    path('profile/delete/<int:id>', views.deleteprofile, name='delete')
]