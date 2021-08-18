from django.db import models
from django.shortcuts import reverse

class News(models.Model):
    title = models.CharField(max_length=128)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('employee_detail_url', kwargs={'id': self.id})