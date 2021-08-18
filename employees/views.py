from django.shortcuts import render, get_object_or_404
from employees.models import Employee
from comments.forms import CommentForm

def employee_list_view(request):
    employees = Employee.objects.all()
    bound_form = CommentForm(request.POST)
    if bound_form.is_valid():
        bound_form.save()
    return render(request, 'employees/index.html', context={'employees': employees,
                                                        'question_form': bound_form})

def employee_detail_view(request, id):
    employee = get_object_or_404(Employee, id=id)
    return render(request, 'employees/employees_detail.html', context={'employee':employee})
