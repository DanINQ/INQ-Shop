from django.urls import path
from bookshop_app.views import *
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', home_page, name='home'),
    path('cart/', cart, name='cart'),
    path('auth/', login_page, name='login'),
    path('account/', account_page, name='account-page'),
    path('sign-up/', sign_up_page, name='sign-up'),
    path('logout/', logout_method, name='logout'),
    path('category/<str:category>', search_category, name='search-category')
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)