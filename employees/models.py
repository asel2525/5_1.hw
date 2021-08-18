from django.db import models
from django.shortcuts import reverse

class Employee(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    job = models.CharField(max_length=128)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('employee_detail_url', kwargs={'id':self.id})

