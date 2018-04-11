from django.db import models

# Create your models here.
class GuestEmail(models.Model):
    email       = models.EmailField()
    update      = models.DateTimeField(auto_now =True)
    timestamp   = models.DateTimeField(auto_now_add =True)

    def __str__(self):
        return self.email
