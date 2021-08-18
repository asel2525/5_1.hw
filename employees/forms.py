from django import forms
from employees.models import Employee

class EmployeeForm(forms.Form):
    class Meta:
        model = Employee
        fields = ['name', 'surname', 'job', ]