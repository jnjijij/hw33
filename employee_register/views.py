from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from .models import Employee
from employee_register.form import EmployeeForm

# Create your views here.
def employee_list(request):
    return render(request,'employee_register/employee_list.html',{'employee_list':Employee.objects.all()})

def employee_form(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            employee = form.save()
            employee.save()
            return redirect('/')
    else:
        form = EmployeeForm()
    return render(request,'employee_register/employee_form.html',{'form':form})

def employee_update(request,id):
    obj = get_object_or_404(Employee, id = id)
    form = EmployeeForm(request.POST or None, instance= obj)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'employee_register/employee_form.html',{'form':form})

def employee_delete(request,id):
    obj = get_object_or_404(Employee, id= id)
    obj.delete()
    return redirect('/')