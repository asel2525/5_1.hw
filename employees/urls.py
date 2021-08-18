from django.urls import path
from employees.views import employee_detail_view, employee_list_view


urlpatterns = [
    path('', employee_list_view, name='employees_list_url'),
    path('<int:id>/', employee_detail_view, name='employee_detail_url'),
]