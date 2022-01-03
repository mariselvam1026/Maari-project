from django.contrib import admin
from demoapp.models import Employee
# Register your models here.
class EmployeeAdmin(admin.ModelAdmin):
    list = ['name', 'age', 'salary']

admin.site.register(Employee,EmployeeAdmin)