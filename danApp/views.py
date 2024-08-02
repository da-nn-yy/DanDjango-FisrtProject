from django.shortcuts import render,redirect
from .forms import ContactForm
from .models import DanApp
# from django.http import HttpResponse
# Create your views here.

# def index(request):
#   # return HttpResponse("Hello, world. You're at the danApp index."
#   tours = DanApp.objects.all()
#   context = {'tours' : tours}
#   return render(request, 'danApp/index.html',context) 


#Home page view func.
def home_view(request):
  return render(request, 'danApp/home.html')

def contact_view(request):
  if request.method =='POST':
    form = ContactForm(request.POST)
    if form.is_valid():
      form.send_email()
      return redirect('contact_success')
  else:
    form = ContactForm()
  context = {'form' : form }
  return render(request,'danApp/contact.html',context)

def contact_success_view(request):
  return(request,'danApp/success.html')