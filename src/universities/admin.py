from django.contrib import admin
from .models import University

class UniversityAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'slug']
    class Meta:
        model = University

# Register your models here.
admin.site.register(University, UniversityAdmin)
