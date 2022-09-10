from django import forms
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django.contrib.auth import get_user_model
from .models import Ticket,User



class NewUserForm(UserCreationForm):
		
	class Meta:
		model = get_user_model()
		fields = ("username","first_name","last_name","email",)

class profile_edit(UserChangeForm):
	class Meta:
		model = get_user_model()
		fields = ("username","first_name","last_name","email",)



class ticketform(forms.ModelForm):

	description = forms.CharField(widget=forms.Textarea)

	class Meta():
		model = Ticket
		fields =['title','subject','priority','description','submittedby']

