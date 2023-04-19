from django.urls import path
from bookshop_app.views import *

urlpatterns = [
    path('', home_page, name='home'),
    path('cart/', cart, name='cart'),
    path('auth/', login, name='login'),
    path('sign-up/', sign_up_page, name='sign-up')
]
