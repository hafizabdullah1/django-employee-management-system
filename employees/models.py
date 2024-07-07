from django.db import models

# Create your models here.

class Employee(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    position = models.CharField(max_length=50, default="developer")
    phone = models.CharField(max_length=20)
    salary = models.IntegerField()
    joinAt = models.DateField(auto_now_add=True)
