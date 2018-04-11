from django.contrib import admin
from .models import Programme

# Register your models here.
class ProgrammeAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'slug']
    class Meta:
        model = Programme

# Register your models here.
admin.site.register(Programme, ProgrammeAdmin)
