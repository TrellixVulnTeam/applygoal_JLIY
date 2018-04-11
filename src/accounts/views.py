from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import ListView
from .forms import  LoginForm, RegisterForm, GuestForm
from django.contrib.auth import authenticate, login, get_user_model
from universities.models import University
from django.utils.http import is_safe_url
from .models import GuestEmail
from django.contrib.auth import login


def guest_register_view(request):
    login_form = GuestForm(request.POST or None)
    context = {
        "form" : login_form
    }
    next_ = request.GET.get('next')
    next_post = request.POST.get('next')
    redirect_path = next_ or next_post or None
    if login_form.is_valid():
        print(login_form.cleaned_data)
        email = login_form.cleaned_data.get("email")
        new_guest_email = GuestEmail.objects.create(email=email)
        request.session['guest_email_id'] = new_guest_email.id
        if is_safe_url(redirect_path, request.get_host()):
            return redirect(redirect_path)
        else:
            return redirect("register/")
    return redirect("lala/")


def login_page(request):
    login_form = LoginForm(request.POST or None)
    context = {
        "form" : login_form
    }
    next_ = request.GET.get('next')
    next_post = request.POST.get('next')
    redirect_path = next_ or next_post or None
    if login_form.is_valid():
        print(login_form.cleaned_data)
        username = login_form.cleaned_data.get("username")
        password = login_form.cleaned_data.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            try:
                 del request.session['guest_email_id']
            except:
                 pass
            if is_safe_url(redirect_path, request.get_host()):
                 return redirect(redirect_path)
            else:
                 return redirect("/")
        else:
            print("error")
    return render(request,'accounts/login.html',context)

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

        # User.objects.create_user()
    return render(request, 'accounts/register.html',context)
