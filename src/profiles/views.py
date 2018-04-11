from django.shortcuts import redirect, render
from django.views.generic import TemplateView
from django.views.generic import CreateView, ListView, UpdateView
from .models import User, Student
from .forms import StudentSignUpForm, TeacherSignUpForm, StudentProfileForm
from django.utils.decorators import method_decorator
from .decorators import student_required
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.urls import reverse_lazy
from django.contrib import messages

def home(request):
    return render(request, 'home.html')


@method_decorator([login_required, student_required], name='dispatch')
class StudentProfile(UpdateView):
    model = Student
    form_class = StudentProfileForm
    template_name='students/profile.html'
    success_url = reverse_lazy('profiles:std')

    def get_object(self):
        return self.request.user.student

    def form_valid(self, form):
        messages.success(self.request, 'aa updated with success!')
        self.object = form.save()
        print("Saved")
        return super().form_valid(form)


class SignUpView(TemplateView):
    template_name = 'registration/signup.html'

class StudentSignUpView(CreateView):
    model = User
    form_class = StudentSignUpForm
    template_name = 'registration/signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'student'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('profiles:std')


class TeacherSignUpView(CreateView):
    model = User
    form_class = TeacherSignUpForm
    template_name = 'registration/signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'teacher'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('teachers:quiz_change_list')
