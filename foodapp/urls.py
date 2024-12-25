from django.urls import path 
from . import views

urlpatterns = [
    path("register/",views.register,name='register'),
    path("",views.login_view,name='login'),
    path("home/",views.home,name='home'),
    path("logout/",views.logout_views,name='logout'),
    path("products/",views.products,name='products'),
    path("carts/",views.carts,name='carts'),
    path("main/",views.main,name='main'),
    path("add/",views.add,name='add'),
    path("delete/<int:id>/",views.delete,name='delete')
    
    
]