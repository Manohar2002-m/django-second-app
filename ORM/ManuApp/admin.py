from django.contrib import admin

# Register your models here.
from django.contrib import admin
from ManuApp.models import Employee

# Register your models here.
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['empno','ename','job','sal','address'];

admin.site.register(Employee,EmployeeAdmin);

