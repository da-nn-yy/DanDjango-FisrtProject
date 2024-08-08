from django.shortcuts import render,redirect
from django.contrib.auth import authenticate , login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin 
from django.views import View
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
      context = {'form':form}
      return render(request, 'accounts/regist.html',{'form':form})

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password) 
        if user is not None:
            login(request, user)
            next_url = request.POST.get('next') or request.GET.get('next') or 'home'
            return redirect(next_url)   
        else:
            error_message = "Invalid Credentials"
            return render(request, 'accounts/login.html', {'error': error_message})
    else:
        return render(request, 'accounts/login.html')
  
def logout_view(request):
  if request.method == "POST":
    logout(request)
    return redirect('login')
  else:
    return redirect('home')

#home page using the decorator
@login_required
def home_view(request):
  return render(request,'auth1_app/home.html')

#protetcted view
class ProtectedView(LoginRequiredMixin, View):
  login_url = '/login/'
  # 'next' - to redirect URL
  redirect_field_name = 'redirect_to'
  def get(self, request):
    return render(request,'regstration/protected.html')