from django.urls import path,re_path

from django.conf import settings
from django.urls import include

from .views import login_page, register_page, guest_register_view
app_name = 'accounts'
urlpatterns = [
    path('login/', login_page, name='login'),
    path('register/', register_page, name='register'),
    path('regis   ter/guest', guest_register_view, name='guest_register_url'),
   ]
