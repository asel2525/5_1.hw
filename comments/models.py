from django.db import models

# Create your models here.
class Comment(models.Model):
    contact = models.CharField(max_length=80)
    question = models.TextField()