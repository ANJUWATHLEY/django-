from django.db import models

# Create your models here. 

class Employee(models.Model):
    name=models.CharField(max_length=50)
    age=models.IntegerField()
    salary=models.IntegerField()
 
class Department(models.Model):
    name = models.CharField(max_length=50)
    head_of_department = models.CharField(max_length=50, default="Not Assigned")  # Default value yaha set karein
    location = models.CharField(max_length=40, default="Unknown")  # Example: location field ka default
    number_of_employees = models.CharField(max_length=40,default=400)
