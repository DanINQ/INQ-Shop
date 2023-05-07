from django.http import HttpResponse
from django.shortcuts import render, redirect

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .forms import CreateUserForm
from django.contrib.auth.decorators import login_required
from .models import *


# Create your views here.


def home_page(request):
    return render(request, 'main.html')


def cart(request):
    return render(request, 'cart.html')


def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Username or password is incorrect')
    return render(request, 'login.html')


@login_required(login_url='login')
def logout_method(request):
    logout(request)
    return redirect('home')


@login_required(login_url='login')
def account_page(request):
    user = User.objects.filter(username=request.user)[0]
    return render(request, 'account_page.html', {'user': user})


def sign_up_page(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account was created')
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, error)

    data = {'form': form}
    return render(request, 'sign-up.html', data)


def search_category(request, category):
    category = Categories.objects.filter(name=category)

    if len(category) != 0:
        books = []

        for category_object in category[0].get_descendants(include_self=True):
            for book in Books.objects.filter(category=category_object.id):
                if book not in books:
                    books.append(book)

        data = {'category': category[0],
                'category_descendants': category[0].get_descendants(
                    include_self=False),
                'books': books
                }
        return render(request, 'search-category.html', data)
    else:
        return HttpResponse(status=404)
