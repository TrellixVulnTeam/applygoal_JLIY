from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()

class ContactForm(forms.Form):
    fullname = forms.CharField(
        widget = forms.TextInput(
            attrs = {
                "placeholder" : "Your name"
            }
        )
    )
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs = {
                "placeholder" : "Your email"
            }
        )
    )
    subject = forms.CharField(
        widget = forms.TextInput(
            attrs = {
                "placeholder" : "Subject"
            }
        )
    )
    message = forms.CharField(
        widget=forms.Textarea(
            attrs = {
                "placeholder" : "Your message"
            }
        ))

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget = forms.PasswordInput)

class RegisterForm(forms.Form):
    CHOICES=(
    ("std", "Student"),
    ("uni", "University"),
    )

    username = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField(widget = forms.PasswordInput)
    status = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect())

    def clean_username(self):
        username = self.cleaned_data.get('username')
        qs = User.objects.filter(username = username)
        if qs.exists():
            raise forms.ValidationError("Username is taken")
        return username

    def clean_email(self):
        email = self.cleaned_data.get('email')
        qs = User.objects.filter(email = email)
        if qs.exists():
            raise forms.ValidationError("email is taken")
        return email
