from django.shortcuts import render,redirect
from demoapp.models import Employee
from demoapp.forms import EmployeeForm
# Create your views here.
def retrive_view(request):
    
    employee = Employee.objects.all()
    return render(request, 'demoapp/index.html',{'employee':employee})

def create(request):
    form = EmployeeForm() 
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/check')

    return render(request, 'demoapp/create.html', {'form':form})

def delete(request,id):
    employee = Employee.objects.get(id=id)
    employee.delete()
    return redirect('/check')


def update(request,id):
    employee = Employee.objects.get(id=id)
    if request.method == 'POST':
        form = EmployeeForm(request.POST,instance=employee)
        if form.is_valid():
            form.save()
            return redirect('/check')
    return render(request, 'demoapp/update.html',{'employee':employee})

