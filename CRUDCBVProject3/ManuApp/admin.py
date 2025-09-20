from django.contrib import admin

# Register your models here.
from django.contrib import admin
from django.db import models
from ManuApp.models import Student


# Create your models here.
class StudentAdmin(admin.ModelAdmin):
    list_display = ['sno', 'sname', 'ssub', 'scollege']


admin.site.register(Student,StudentAdmin)


