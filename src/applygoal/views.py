from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import ListView
from .forms import ContactForm, LoginForm, RegisterForm
from django.contrib.auth import authenticate, login, get_user_model
from universities.models import University

def home_page (request):
    reg_form = RegisterForm(request.POST or None)
    context = {
        "form": reg_form
    }
    if reg_form.is_valid():
        print(reg_form.cleaned_data)
        username = reg_form.cleaned_data.get("username")
        password = reg_form.cleaned_data.get("password")
        email = reg_form.cleaned_data.get("email")
        status = reg_form.cleaned_data.get("status")
        new_user = User.objects.create_user( username, password, email)
        mystatus = request.POST["status"]
        print(new_user)
        print(mystatus)
        if mystatus == 'uni':
            print("nailed it")
        # User.objects.create_user(

    return render(request, 'homepage.html' ,context)

# class HomeView(ListView):
#
#     template_name="view.html"
#
#     def get_context_data(self, *args, **kwargs):
#         context = super(HomeView, self).get_context_data(*args, **kwargs)
#         query = self.request.GET.get('q')
#         context['query'] = query
#         # SearchQuery.objects.create(query=query)
#         return context
#
#     def get_queryset(self, *args, **kwargs):
#         request = self.request
#         method_dict = request.GET
#         query = method_dict.get('q', None) # method_dict['q']
#         if query is not None:
#             return University.objects.filter(title__icontains=query)
#         return University.objects.all()


def contact_page (request):
    contact_form = ContactForm(request.POST or None)
    context = {
        "title" : "Contact",
        "form": contact_form
    }
    if contact_form.is_valid():
        print (contact_form.cleaned_data)
    return render(request, 'Contact/contact.html',context)

def login_page(request):
    login_form = LoginForm(request.POST or None)
    context = {
        "form" : login_form
    }
    if login_form.is_valid():
        print(login_form.cleaned_data)
        username = login_form.cleaned_data.get("username")
        password = login_form.cleaned_data.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            context['form'] = LoginForm()
            return redirect("/login")
        else:
            print("error")
    return render(request,'Auth/login.html',context)

User = get_user_model()
def register_page (request):
    reg_form = RegisterForm(request.POST or None)
    context = {
        "form": reg_form
    }
    if reg_form.is_valid():
        print(reg_form.cleaned_data)
        username = reg_form.cleaned_data.get("username")
        password = reg_form.cleaned_data.get("password")
        email = reg_form.cleaned_data.get("email")
        status = reg_form.cleaned_data.get("status")
        new_user = User.objects.create_user( username, password, email)
        mystatus = request.POST["status"]
        print(new_user)
        print(mystatus)
        if mystatus == 'uni':
            print("nailed it")
        # User.objects.create_user()
    return render(request, "auth/register.html",context)
