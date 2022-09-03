from email.policy import default
from django import forms
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django.forms import ModelForm
from django.contrib.auth import get_user_model, get_user
from .models import Ticket
from django.contrib.auth.models import User

class NewUserForm(UserCreationForm):
		
	class Meta:
		model = get_user_model()
		fields = ("username","first_name","last_name","email",)

class profile_edit(UserChangeForm):
	class Meta:
		model = get_user_model()
		fields = ("username","first_name","last_name","email",)

Priority_Choices = [
    ('LOW','Low'),
    ('MEDIUM','Medium'),
    ('HIGH','High'),
    ('IMMEDIATE','Immediate'),
]

class ticketform(forms.ModelForm):
	description = forms.CharField(widget=forms.Textarea)

	class Meta:
		model = Ticket
		fields =['title','subject','priority','description','submittedby']
  