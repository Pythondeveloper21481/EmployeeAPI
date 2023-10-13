from django.db import models

# Create your models here.

class Departements(models.Model):
    DepartementId = models.AutoField(primary_key=True)
    DepartementName = models.CharField(max_length=100)

class Employees(models.Model):
    EmployeeId = models.AutoField(primary_key=True)
    EmployeeName = models.CharField(max_length=100)
    Departement = models.CharField(max_length=100)
    DateOfJoining = models.DateField()
    PhotoFileName = models.CharField(max_length=100)
    