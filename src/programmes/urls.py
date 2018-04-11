from django.urls import path,re_path

from django.conf import settings
from django.urls import include

from .views import prog_list_view,prog_detail_view, ProgrammeDetailSlugView
app_name = 'programmes'
urlpatterns = [
    path('', prog_list_view, name='home'),
    path('details/<int:pk>/', prog_detail_view, name='details'),
    # path('lsview/', UniversityListView.as_view(), name='universities'),
    # path('<int:pk>/', university_detail_view, name = 'details'),
    path('<slug:slug>/', ProgrammeDetailSlugView.as_view(), name = 'details'),
    # path('details/<int:pk>/', UniversityDetailView.as_view(), name='details'),

   ]
