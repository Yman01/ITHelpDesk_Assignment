from django.shortcuts import render,redirect
from django.contrib.auth import login,authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponse
from django.template import loader

from .models import Ticket,User
from .forms import NewUserForm, ticketform, profile_edit

def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				return redirect("home")
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request=request, template_name="login.html", context={"login_form":form})

def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("home")
		else:
			messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	return render (request=request, template_name="register.html", context={"register_form":form})

def getuser(request):

	model = Ticket
	form_class = ticketform

	def get_form_kwargs(self):
		kwargs = super(getuser, self).get_form_kwargs()
		kwargs.update({'user':self.request.user})
		return kwargs

@login_required
def ticket(request):
	if request.POST:
		form = ticketform(request.POST)
		if form.is_valid():
			form.save()
		return redirect("home")
	return render(request,'ticket.html',{'ticket_form':ticketform})

def homeview(request):
	
	return render(request,'home.html')

def tickettable(request):	
	data = Ticket.objects.all().values()
	template = loader.get_template('table.html')
	context = {
		'data':data,
	}
	return HttpResponse(template.render(context,request))

def view_profile(request):
	args = {'user':request.user}
	return render(request, 'profile.html',args)

def edit_profile(request):
	if request.POST:
		form = profile_edit(request.POST)
		if form.is_valid():
			user = form.save()
			logout(request,user)
		return redirect ("home")
	return render(request, 'profile_edit.html',{'profile_edit':profile_edit})