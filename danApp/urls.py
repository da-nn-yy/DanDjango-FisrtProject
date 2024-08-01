from django.urls import path
from . import views

#Define a list of URL patterns

urlpatterns = [
  path('', views.index,name='index'),
]
