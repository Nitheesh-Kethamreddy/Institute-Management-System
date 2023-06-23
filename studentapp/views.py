from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, redirect
from studentapp.models import *


# Create your views here.
def home(request):
    return render(request,'base.html')


def log_fun(request):
    if request.method == "POST":
        name = request.POST['tbname']
        password = request.POST['pswd']
        user = authenticate(username=name, password=password)

        if user is not None:
            if user.is_superuser:
                return redirect('home')
            else:
                return render(request, 'login.html', {'msg': True})
        else:
            return render(request, 'login.html', {'msg': True})
    else:
        return render(request, 'login.html', {'msg': False})

def sign_fun(request):
    if request.method == "POST":
        name = request.POST['tbname']
        email = request.POST['tbemail']
        password = request.POST['pswd']
        if User.objects.filter(Q(username=name) | Q(email=email) | Q(password=password)):
            data = {'msg': True}
            return render(request, 'signup.html', data)
        else:
            user = User.objects.create_superuser(username=name, password=password, email=email)
            user.save()
            return redirect('login')

    return render(request, 'signup.html', {'msg': False})


def home_fun(request):
    return render(request,'home.html')


def add_fun(request):
    c1 = City.objects.all()
    if request.method == 'POST':
        s1 = Student()
        s1.name = request.POST['txtName']
        s1.place =City.objects.get(city = request.POST['ddlplace'])
        s1.phone = request.POST['txtPhno']
        s1.age = request.POST['txtAge']
        s1.email = request.POST['txtEmail']
        s1.gender = request.POST['txtGen']
        s1.save()
        print(s1)
        return render(request,'success.html')
    return render(request,'add.html',{'place':c1})





def display_fun(request):

    d1=Student.objects.all()
    return render(request,'display.html',{"data":d1})


def logout_fun(request):
    return render(request,'base.html')


def update_fun(request,id):
    c1 = City.objects.all()
    s1 = Student.objects.get(id=id)
    if request.method == "POST":
        s1.name = request.POST['txtName']
        s1.place = City.objects.get(city=request.POST['ddlplace'])
        s1.phone = request.POST['txtPhno']
        s1.age = request.POST['txtAge']
        s1.email = request.POST['txtEmail']
        s1.gender = request.POST['txtGen']
        s1.save()
        return redirect('display')
    return render(request, 'update.html', {"d_data": s1,"data":c1})


def delete_fun(request,id):
    c1 = Student.objects.get(id=id)
    c1.delete()
    return redirect('display')