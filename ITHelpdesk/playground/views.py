import re
from tkinter.messagebox import RETRY
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect



def loginpage(request):
    return render(request,'loginpage.html')

def signuppage(request):
    return render(request,'signup.html')


