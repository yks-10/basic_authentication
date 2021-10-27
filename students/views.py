from django.shortcuts import render,redirect 
from .forms import *
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required

def index(request):
	return render(request, "students/index.html")


def signupuser(request):
	if request.method=="GET":
		return render(request, "students/signup.html", {'form':Students()})
	else:
		if request.POST['password1']== request.POST['password2']:
			try:
				user=User.objects.create_user(username=request.POST['roll_number'], password=request.POST['password1'])
				user.save()
				login(request, user)
				return redirect('data')
			except IntegrityError:
				return render(request, "students/signup.html", {'form':Students(),'error':'USER NAME ALREADY TAKEN'})

def loginuser(request):
	if request.method=="GET":
		return render(request, "students/login.html", {'form':Studentlog()})
	else:
		user= authenticate(request, username=request.POST['roll_number'], password=request.POST['password'])
		if user is None:
			print("logged in")
			return render(request, "students/data.html")
		else:
			
			return redirect('data')


def data(request):
	return render(request, "students/data.html")


def logoutuser(request):
	if request.method=="POST":
		print("logout")
		logout(request)
		return redirect('index')