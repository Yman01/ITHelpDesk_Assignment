from django.contrib.auth.hashers import check_password
from django.contrib.auth.backends import BaseBackend
from django.shortcuts import render
from models import User
from forms import NewUserForm

class authbackend(BaseBackend):
    def authenticate(self, request, username = None, password = None):
        login_valid = ( NewUserForm.username == User.username)
        pwd_valid  = check_password(password,User.password)
        if login_valid and pwd_valid:
            try:
                user = User.objects.get(username=username)

            except User.DoesNotExist:
                return render(request, "login.html")