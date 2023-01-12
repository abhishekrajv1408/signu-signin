from django.db import models

# Create your models here.

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.utils import timezone
from django.views import generic
from django import forms


# Create your views here.

class SignUpView(generic.CreateView):
    # email=forms.EmailField(max_length=254, help_text='Please Enter a valid Email id' ,primary_key=True)
    form_calss=UserCreationForm
    success_url=reverse_lazy('login')
    template_name = 'registration/signup.html'

# class Register(models.Model):

class Post(models.Model):
    titel=models.CharField(max_length=100)
    content=models.TextField()
    date=models.DateTimeField(default=timezone.now)
    author=models.ForeignKey(User, on_delete=models.CASCADE)