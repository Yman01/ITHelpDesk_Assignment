from django.db import models
from django.forms import DateField, ModelForm, ValidationError

class User(models.Model):
    fname = models.CharField(max_length=100,verbose_name= "First Name")
    lname = models.CharField(max_length=100,verbose_name= "Last Name")
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.email

Priority_Choices = [
    ('LOW','Low'),
    ('MEDIUM','Medium'),
    ('HIGH','High'),
    ('IMMEDIATE','Immediate'),
]

class Ticket(models.Model):
    title = models.CharField(max_length=100)
    Subject = models.CharField(max_length=100,)
    Priority = models.CharField(max_length= 100, choices=Priority_Choices)
    datecreated = models.DateTimeField(auto_now_add= True)
    Description = models.CharField(max_length=10000)

    def __str__(self):
        return self.title
