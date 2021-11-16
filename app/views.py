from django.shortcuts import render

from django.http import HttpResponse

def login(request):
	return render(request,"login.html")

#def login1(request):
#	return render(request,"mgmt.html")

def index(request):	
	return render(request,"index.html")