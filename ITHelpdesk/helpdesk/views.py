from django.shortcuts import render,redirect
from django.contrib.auth import login,authenticate, logout, get_user_model, get_user
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader
from django.urls import reverse

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

@login_required
def ticket(request):
	# args = {'user':request.user}
	print(request)
	if request.POST:
		print(get_user(request))
		request.POST = request.POST.copy()
		request.POST.__setitem__('submittedby',get_user(request))
		# print(request.POST)
		form = ticketform(request.POST)
		# form.submittedby.initial = get_user_model()
		# form.submittedby.initial="abc"
		if form.is_valid():
				# form.instance.submittedby = request.user
				form.save()
				return redirect("home")			
	else:
		form = ticketform(initial={'submittedby':get_user(request).get_username()})
		print(form)
		# form.submittedby.initial="abc"
		return render(request,'ticket.html',{'ticket_form':ticketform})

def homeview(request):
	data = Ticket.objects.all().values()
	template = loader.get_template('home.html')
	context = {
		'data':data,
	}
	return HttpResponse(template.render(context,request))


def updateticket(request,id):
	thisticket = Ticket.objects.get(id=id)
	template = loader.get_template('updateticket.html')
	context = {
		'thisticket':thisticket,
	}
	return HttpResponse(template.render(context,request))

def updaterecord(request,id):
	title = request.POST['title']
	subject = request.POST['subject']
	priority = request.POST['priority']
	description = request.POST['description']
	thisticket = Ticket.objects.get(id=id)
	thisticket.title = title
	thisticket.subject = subject
	thisticket.priority = priority
	thisticket.description = description
	thisticket.save()
	return HttpResponseRedirect(reverse('home'))

def delete(request,id):
	thisticket = Ticket.objects.get(id=id)
	thisticket.delete()
	return HttpResponseRedirect(reverse('home'))

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