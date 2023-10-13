from rest_framework import serializers
from EmployeeApp.models import Departements, Employees


class DepartementSerialiser(serializers.ModelSerializer):
    class Meta:
       model = Departements
       fields = ('DepartementId', 'DepartementName') 

class EmployeesSerialiser(serializers.ModelSerializer):
    class Meta:
       model = Employees
       fields = ('EmployeeId', 'EmployeeName', 'Departement','DateOfJoining', 'PhotoFileName') 