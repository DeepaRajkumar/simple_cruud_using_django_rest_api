from django.db import models
class Employee(models.Model):
    emp_name=models.CharField(max_length=20)
    emp_designation=models.CharField(max_length=20)
    emp_salary=models.CharField(max_length=20)
    emp_address=models.CharField(max_length=20)

# Create your models here.
