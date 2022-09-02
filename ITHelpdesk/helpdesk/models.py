from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.contrib.auth import get_user_model

class User(AbstractUser):
    username = models.CharField(max_length=100,unique=True,blank=False)
    email = models.EmailField(max_length=100)
    
    def __str__(self):
            return self.username


Priority_Choices = [
    ('LOW','Low'),
    ('MEDIUM','Medium'),
    ('HIGH','High'),
    ('IMMEDIATE','Immediate'),
]

class Ticket(models.Model):
    title = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    priority = models.CharField(max_length= 100, choices=Priority_Choices)
    datecreated = models.DateTimeField(auto_now_add= True)
    description = models.CharField(max_length=10000)
    submittedby = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
