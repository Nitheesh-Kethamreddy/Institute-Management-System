
from django.urls import path

from studentapp import views

urlpatterns =[
    path('',views.home),
    path('login',views.log_fun,name='login'),
    path('signup',views.sign_fun,name='signup'),
    path('home',views.home_fun,name='home'),
    path('add',views.add_fun,name='add'),
    path('display',views.display_fun,name='display'),
    path('update/<int:id>',views.update_fun,name='update'),
    path('delete/<int:id>',views.delete_fun,name='delete'),
    path('logout',views.logout_fun,name='logout')
]