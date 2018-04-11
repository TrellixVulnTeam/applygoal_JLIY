from django.urls import path,re_path

from django.conf import settings
from django.urls import include

from .views import UniversityListView, university_list_view, UniversityDetailView, university_detail_view, UniversityDetailSlugView
app_name = 'universities'
urlpatterns = [
    path('a/', university_list_view, name='home1'),
    path('', UniversityListView.as_view(), name='home'),
    path('<int:pk>/', university_detail_view, name = 'details'),
    path('<slug:slug>/', UniversityDetailSlugView.as_view(), name = 'details'),
    path('details/<int:pk>/', UniversityDetailView.as_view(), name='details'),

   ]
