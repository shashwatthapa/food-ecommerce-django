from django.urls import path 
from . import views

urlpatterns = [
    path("register/",views.register,name='register'),
    path("",views.login_view,name='login'),
    path("home/",views.home,name='home'),
    path("logout/",views.logout_views,name='logout')
    
]