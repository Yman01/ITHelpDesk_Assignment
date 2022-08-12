from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm

def loginpage(request):
    return HttpResponse("Login to view/submit tickets")

def signup(request):
    return 

