"""HelpDeskTool URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path , include
from django.views.generic.base import TemplateView
from helpdesk import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('helpdesk/',include('helpdesk.urls')),
    path('__debug__/', include('debug_toolbar.urls')),
    path('/accounts/', include('django.contrib.auth.urls')),
    path('', views.homeview,name='home'),
    path("register",views.register_request, name="register"),
    path("login", views.login_request, name="login"),
    path("tickets",views.ticket,name='tickets'),
    path("profile",views.view_profile,name='profile'),
    path("profile/edit",views.edit_profile,name='edit_profile'),
    path('update/<int:id>', views.updateticket, name='update'),
    path('update/updaterecord/<int:id>', views.updaterecord, name='updaterecord'),
    path('delete/<int:id>', views.delete, name='delete')
]

