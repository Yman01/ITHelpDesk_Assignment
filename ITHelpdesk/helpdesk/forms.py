from django import forms
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django.forms import ModelForm
from .models import Priority_Choices,Ticket,User



class NewUserForm(UserCreationForm):
		
	class Meta:
		model = User
		fields = ("username","first_name","last_name","email",)

class profile_edit(UserChangeForm):
	class Meta:
		model = User
		fields = ("username","first_name","last_name","email",)



class ticketform(ModelForm):

	title = forms.TextInput()
	subject = forms.TextInput()
	priority = forms.ChoiceField(choices=Priority_Choices)
	description = forms.CharField(widget=forms.Textarea)
	submittedby = forms.ModelChoiceField(queryset= User.objects.filter())
	print(User.objects.all())

	class Meta:
		model = Ticket
		fields = ['title','subject','priority','description','submittedby']

