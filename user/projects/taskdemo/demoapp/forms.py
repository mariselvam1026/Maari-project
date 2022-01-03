from django import forms
from django import forms
from demoapp.models import Employee

# Create your models here.
class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'
   
   