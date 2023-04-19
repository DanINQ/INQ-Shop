from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def home_page(request):
	return render(request, 'main.html')


def cart(request):
	return render(request, 'cart.html')


def login(request):
	return render(request, 'login.html')


def sign_up_page(request):
	return render(request, 'sign-up.html')