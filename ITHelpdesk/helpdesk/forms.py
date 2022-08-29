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
	description = forms.Textarea(attrs={'cols':80,'rows':20})
	submittedby = forms.ModelChoiceField(queryset= User.objects.all())

	def __init__(self,*args,user= None,**kwargs):
		
		super().__init__(*args,**kwargs)
		if user:
			submittedby = self.fields['submittedby']
			submittedby.queryset = submittedby.queryset.filter(submittedby=user)

	class Meta:
		model = Ticket
		fields = ['title','subject','priority','description','submittedby']


