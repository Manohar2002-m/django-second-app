from django.contrib import admin

# Register your models here.
from django.contrib import admin
from django.db import models
from ManuApp.models import Employee
#Create your models here.
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['eno','ename','esal','eaddr']

admin.site.register(Employee,EmployeeAdmin)
