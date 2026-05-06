from django.shortcuts import render,redirect
from .models import Employee
# Create your views here.

def add_employee(request):
    if request.method == "POST":
        Employee.objects.create(
            e_name = request.POST['e_name'],
            e_number = request.POST['e_number'],
            e_email = request.POST['e_email'],
            e_salary = request.POST['e_salary'],
            e_company = request.POST['e_company'],
            e_image = request.FILES['e_image']
        )
        return redirect('view_employee_details')
    return render(request,'add.html')

def view_employee_details(request):
    employees = Employee.objects.all()
    return render(request,'view.html',{'employees':employees})

def get_employee_details(request,id):
    employee = Employee.objects.get(id=id)
    return render(request,'get.html',{'employee':employee})


def register_page(request):
    return render(request,'register.html')

def delete_employee(request,id):
    Employee.objects.get(id=id).delete()
    return redirect('view_employee_details')