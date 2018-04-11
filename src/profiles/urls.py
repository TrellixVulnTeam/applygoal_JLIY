from django.urls import include, path
from .views import (home, SignUpView, StudentSignUpView,TeacherSignUpView,StudentProfile)
app_name = 'profiles'
urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('student/', StudentProfile.as_view(), name='std'),
    # path('accounts/', include('django.contrib.auth.urls')),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('signup/student/', StudentSignUpView.as_view(), name='student_signup'),
    path('signup/university/', TeacherSignUpView.as_view(), name='teacher_signup'),
    # path('', TeacherSignUpView.as_view(), name='student'),
    ]
