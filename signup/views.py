from django.contrib.auth.forms import UserCreationForm
# from django.urls import reverse_lazy
# from django.views import generic
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.http import HttpResponse
from signup.forms import SignUpForm
from django.core.exceptions import ValidationError

from home.models import Post

 
def signup(request):
    if request.method=='POST':
        form=SignUpForm(request.POST)
        form.order_fields(field_order=['first_name','last_name','email','username','password1','password2',])
        if form.is_valid():
            form.save()
            return redirect ('http://127.0.0.1:8000/accounts/login/')
        else:
            return HttpResponse("Something Wrong")
    else:
        form=SignUpForm()
        form.order_fields(field_order=['first_name','last_name','email','username','password1','password2',])
        return render(request,'registration/signup.html',{'form':form})