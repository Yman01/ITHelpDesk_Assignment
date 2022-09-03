from tkinter import NE
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import UserChangeForm,NewUserForm
from .models import Ticket
from django.contrib.auth import get_user_model

class NewUserAdmin(UserAdmin):
    add_form = NewUserForm
    form = UserChangeForm
    model = get_user_model()
    list_display = ["username","email"]

admin.site.register(Ticket)
