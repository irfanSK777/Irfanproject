from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Employee
from django.contrib import messages
from Employee.forms import *

# Create your views here.
# superuser useernane = irfan
# password = helloworld


def register(request):
    if request.method == 'POST':
        form = Registerpage(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'SUCCESS')
            return redirect ('/')
    else:
        form = Registerpage()
    return render(request, 'register.html', {'form':form})


def empDetails(request):
    try:
        print(request.POST)
        if request.method == 'POST':
            eno = request.POST['no']
            ename = request.POST['name']
            salary = request.POST['salary']
            print('Creating object')
            emp = Employee.objects.create(
                empno=eno, empname=ename, salary=salary)

            print(emp)

            print(eno, ename, salary)
            messages.success(request, 'Successfully inserted')
    except Exception:
        messages.error(request, 'Something went wrong')
        messages.info(request, 'It is looking like primary key issue')
    return render(request, 'home.html')

# DATA FETCH PAGE

def fetchData(request):
    if request.method == 'GET':
        return render(request, 'empdetails.html')

    elif 'all' in request.POST:
        data = Employee.objects.all()
        context = {
            'info': data
        }
        return render(request, 'output.html', context)

def search_through_number(request):
    if request.method == 'POST':
        eno = request.POST['sno']
        data = Employee.objects.filter(empno=eno)
        context = {
            'info': data
        }
        print(context)
        return render(request, 'fetch.html',context)
    return render(request, 'fetch.html')


def deleteEmp(request):
    no = request.POST['eno']
    Employee.objects.filter(empno=no).delete()
    return render(request, 'Result.html')

# def Result(request):
#     return render(request, 'Result.html')

