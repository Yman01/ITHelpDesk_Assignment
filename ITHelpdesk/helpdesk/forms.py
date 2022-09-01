from django import forms
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django.forms import ModelForm

from .models import Ticket,User



class NewUserForm(UserCreationForm):
		
	class Meta:
		model = User
		fields = ("username","first_name","last_name","email",)

class profile_edit(UserChangeForm):
	class Meta:
		model = User
		fields = ("username","first_name","last_name","email",)



class ticketform(forms.ModelForm):

	description = forms.CharField(widget=forms.Textarea)
	submittedby = forms.ModelChoiceField(queryset= User.objects.exclude(username = User.is_authenticated))

	class Meta():
		model = Ticket
		fields =['title','subject','priority','description','submittedby']
		exclude = ['submittedby']
	# def __init__(self,*args,**kwargs):
	# 	super(ticketform,self).__init__(*args,**kwargs)
	# 	thisuser = User.is_authenticated
	# 	self.fields['submittedby'].queryset = User.objects.filter(username = thisuser)

