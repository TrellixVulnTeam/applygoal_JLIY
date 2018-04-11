"""applygoal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/dev/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LogoutView
from django.contrib import admin
from accounts.views import login_page
from django.urls import path, include ,re_path
from .views import home_page,contact_page
urlpatterns = [
    path('universities/', include('universities.urls', namespace='universities')),
    path('programmes/', include('programmes.urls', namespace='programmes')),
    path('search/', include('search.urls', namespace='search')),
    path('cart/', include('cart.urls', namespace='cart')),
    path('accounts/', include('accounts.urls', namespace='accounts')),
    path('', home_page, name='home'),
    path('profiles/', include('profiles.urls',namespace='profiles')),
    # path('contact/', contact_page),
    path('logout/', LogoutView.as_view(), name='logout'),
    # path('login/', login_page, name='logout'),
    # path('register/', register_page),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
