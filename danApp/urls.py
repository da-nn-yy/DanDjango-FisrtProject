from django.urls import include, path
from . import views

#Define a list of URL patterns

urlpatterns = [
  path('', views.index,name='index'),
]
