from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from django.forms.utils import ValidationError
# from django.forms import extras
from .models import ( Student,  User)


class StudentSignUpForm(UserCreationForm):
    # degree = forms.ModelMultipleChoiceField(
    #     queryset=Subject.objects.all(),
    #     widget=forms.CheckboxSelectMultiple,
    #     required=True
    # )
    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_student = True
        user.save()
        student = Student.objects.create(user=user)

        return user

class TeacherSignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_teacher = True
        if commit:
            user.save()
        return user




class StudentProfileForm(forms.ModelForm):
    image = forms.ImageField(label='Company Logo',required=False,  widget=forms.FileInput)
    class Meta:
        model = Student
        fields = ('fullname','application','email','country','city','birth_date','image')

        widgets = {
            'fullname': forms.TextInput(
                attrs = {
                    "placeholder" : "Your name!!!"
                }
            ),

        }
