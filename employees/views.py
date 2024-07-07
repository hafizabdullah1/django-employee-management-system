from django.shortcuts import render, redirect
from .models import *
from .forms import EmployeeForm

# Create your views here.

def home(request):
    employees = Employee.objects.all()
    return render(request,"index.html", {'employees': employees})


def create_page(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = EmployeeForm()
    return render(request, "create.html")


def update_page(request, id):
    employee = Employee.objects.get(id = id)
    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = EmployeeForm(instance=employee)
    return render(request, "update.html", {'form': form})
        
def delete_page(request, id):
    employee = Employee.objects.get(id = id)
    if request.method == 'POST':
        employee.delete()
        return redirect('home')
    return render(request, "delete.html", {'employee': employee})
