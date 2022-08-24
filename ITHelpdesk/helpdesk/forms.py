from django import forms
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
# from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import Priority_Choices,Ticket,User


# class NewUserForm(UserCreationForm):
# 	email = forms.EmailField(required=True)

# 	class Meta:
# 		model = User
# 		fields = ("username", "email", "password1", "password2",)

# 	def save(self, commit=True):
# 		user = super(NewUserForm, self).save(commit=False)
# 		user.email = self.cleaned_data['email']
# 		if commit:
# 			user.save()
# 		return user

class NewUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ("username","first_name","last_name","email",)

class UserChangeFrom(UserChangeForm):
	class Meta:
		model = User
		fields = ("username","first_name","last_name","email",)

class ticketform(ModelForm):
	title = forms.TextInput()
	subject = forms.TextInput()
	priority = forms.ChoiceField(choices=Priority_Choices)
	description = forms.Textarea()

	class Meta:
		model = Ticket
		fields = ['title','subject','priority','description']


