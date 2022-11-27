from django.contrib import admin
from Employee.models import *
# Register your models here.
admin.site.register(Employee)
admin.site.register(Projects)
admin.site.register(Salary)
# admin.site.register(Skill)