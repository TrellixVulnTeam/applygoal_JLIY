import random
import os
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from universities.utils import unique_slug_generator
from django.db import models
from django.db.models import Q
from django.db.models.signals import pre_save, post_save
from django.urls import reverse
from django.contrib.auth.models import AbstractUser

def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext

def upload_image_path(instance, filename):
    # print(instance)
    #print(filename)
    new_filename = random.randint(1,3910209312)
    name, ext = get_filename_ext(filename)
    final_filename = '{new_filename}{ext}'.format(new_filename=new_filename, ext=ext)
    return "profiles/{new_filename}/{final_filename}".format(
            new_filename=new_filename,
            final_filename=final_filename
            )


class User(AbstractUser):
    is_student = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)

class Student(models.Model):
    user        = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    image       = models.ImageField(upload_to=upload_image_path,null=True,blank=True)
    fullname    = models.CharField(max_length=120)
    email       = models.EmailField(blank=True, null=True)
    birth_date  = models.DateField(blank=True, null=True)
    country     = models.CharField(max_length=120)
    city        = models.CharField(max_length=120)


    Bachelor    = 'B'
    Master      = 'M'
    application_choices = (
        (Bachelor, 'Bachelor'),
        (Master, 'Master'),

    )
    application = models.CharField(
     max_length=10,
     choices =application_choices,
     default = Bachelor
    )
    def __str__(self):
        return self.user.username


class Certificate(models.Model):
    user        = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)



class Profile(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='quizzes')
    name = models.CharField(max_length=255)
    Surname = models.CharField(max_length=255)

    def __str__(self):
        return self.name
