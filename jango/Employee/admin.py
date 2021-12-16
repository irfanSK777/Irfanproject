from django.contrib import admin
from .models import *

# Register your models here.


class EmpAdmin(admin.ModelAdmin):
        model = Employee
        list_display = ['empno','empname','salary']

admin.site.register(Employee,EmpAdmin)