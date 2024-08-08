from django.urls import path
from . import views

urlpatterns = [
    path('',views.home_view,name='home'),
    path('login/',views.login_view,name='login'),
    path('logout/',views.logout_view,name='logout'),
    path('regist/',views.register_view,name='register'),
    path('ptotected/',views.ProtectedView.as_view(),name='protected'),
]