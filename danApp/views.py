from django.shortcuts import render

from .models import DanApp
# from django.http import HttpResponse
# Create your views here.

def index(request):
  # return HttpResponse("Hello, world. You're at the danApp index."
  tours = DanApp.objects.all()
  context = {'tours' : tours}
  return render(request, 'danApp/index.html',context) 