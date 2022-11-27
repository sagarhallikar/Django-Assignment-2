from django.db import models

# Create your models here.
   

class Employee(models.Model):
    
    Name = models.CharField(max_length=255)
    Emp_Id = models.CharField(max_length=100)
    Address = models.CharField(max_length=255)
    Email = models.EmailField()
    Contact = models.CharField(max_length=15)
  
  
  
    def __str__(self):  
        return self.Name

class Projects(models.Model):
    title=models.CharField(max_length=100)
    employees=models.ForeignKey(Employee,on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Salary(models.Model):
    salary=models.CharField(max_length=10)
    employee=models.ManyToManyField(Employee)
   

# class Skill(models.Model):
#     skill=models.CharField(max_length=100)
#     employee=models.ManyToManyField(Employee)

#     def __str__(self):
#         return self.skill