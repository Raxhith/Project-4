from django.shortcuts import render
from django.http import HttpResponse

def Nat_gam(request):
	data = '<h1>The national game is HOCKEY</h1>'
	return HttpResponse(data)

def Nat_ani(request):
	data = '<h1>The national animal is TIGER</h1>'
	return HttpResponse(data)

def Nat_flo(request):
	data = '<h1>The national flower is LOTUS</h1>'
	return HttpResponse(data)
