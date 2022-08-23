from django.db import models
from django.forms import DateField, ModelForm, ValidationError

class User(models.Model):
    fname = models.CharField(max_length=100,verbose_name= "First Name")
    lname = models.CharField(max_length=100,verbose_name= "Last Name")
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100, unique=True)
    isstaff = models.BooleanField(default=False,blank=True, editable=True)


Priority_Choices = [
    ('LOW','Low'),
    ('MEDIUM','Medium'),
    ('HIGH','High'),
    ('IMMEDIATE','Immediate'),
]

class Ticket(models.Model):
    title = models.CharField(max_length=100)
    subject = models.CharField(max_length=100,)
    priority = models.CharField(max_length= 100, choices=Priority_Choices)
    datecreated = models.DateTimeField(auto_now_add= True)
    description = models.CharField(max_length=10000)

    def __str__(self):
        return self.title
