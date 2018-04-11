from django.urls import path,re_path

from django.conf import settings
from django.urls import include

app_name = 'search'
from .views import(
        SearchListView,
    )

urlpatterns = [
    path('', SearchListView.as_view(), name='query'),
    ]
