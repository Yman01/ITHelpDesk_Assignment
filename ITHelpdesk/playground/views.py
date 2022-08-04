import re
from django.shortcuts import render
from django.http import HttpResponse


def loginpage(request):
    return render(request,'loginpage.html')

def signuppage(request):
    return render(request,'signup.html')