from django.shortcuts import render, redirect 
from django.contrib.auth.models import User
#from django.contrib import auth
from django.contrib.auth import authenticate, login


def login_user(request):
	if request.method == "POST":
		print(request.POST['username'])
		user = authenticate(username=request.POST['username'],password=request.POST['password'])
		print('User-details', user)
		if user is not None:
			login(request,user)
			return redirect('index')
		else:
			return render(request, 'login.html', {'error': 'Username or Password is incorrect !'})
	else:
		return render(request, 'login.html')


	#return render(request, 'login.html')

def index(request):

	return render(request ,'index.html')