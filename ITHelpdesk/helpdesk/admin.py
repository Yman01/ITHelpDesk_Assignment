from tkinter import NE
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import UserChangeForm,NewUserForm
from .models import User,Ticket

class NewUserAdmin(UserAdmin):
    add_form = NewUserForm
    form = UserChangeForm
    model = User
    list_display = ["username","email"]

admin.site.register(User)
admin.site.register(Ticket)
