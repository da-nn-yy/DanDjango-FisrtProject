from django.shortcuts import render,redirect
from django.contrib.auth import authenticate , login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.view import View
from django.contrib.auth.models import User
from .forms import RegisterForm


def register_view(request):
  if request.method == "POST":
    form = RegisterForm(request.POST)
    if form.is_valid():
      username = form.cleaned_data.get("username")
      password = form.cleaned_data.get("password")
      user = User.objects.create_user(username=username,password=password) 
      login(request,user)
      return redirect('home')
    else:
      form = RegisterForm()
      return render(request, 'accounts/regist.html',{'form':form})

def login_view(request):
  pass
def logout_view(request):
  pass

#home page using the decorator

def home_view(request):
  pass