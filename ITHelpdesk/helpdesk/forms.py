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

Priority_Choices = [
    ('LOW','Low'),
    ('MEDIUM','Medium'),
    ('HIGH','High'),
    ('IMMEDIATE','Immediate'),
]

class ticketform(forms.ModelForm):
	description = forms.CharField(widget=forms.Textarea)
	title= forms.CharField(max_length=100)
	subject = forms.CharField(max_length=100)
	priority = forms.ChoiceField(choices=Priority_Choices)
	# datecreated = forms.DateTimeField(auto_now_add= True)
	submittedby = forms.CharField(max_length=10000,widget=forms.HiddenInput)
	# submittedby = forms.CharField(widget=forms.TextInput(attrs=DEFAULT_ATR))
	# submittedby = forms.CharField(initial='ABCD')

	class Meta():
		model = Ticket
		fields =['title','subject','priority','description','submittedby']
		# exclude = ['submittedby']
	# def __init__(self,*args,**kwargs):
	# 	super(ticketform,self).__init__(*args,**kwargs)
	# 	thisuser = User.is_authenticated
	# 	self.fields['submittedby'].queryset = User.objects.filter(username = thisuser)

