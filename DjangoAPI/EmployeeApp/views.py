from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
# Create your views here.
from EmployeeApp.models import Departements, Employees
from EmployeeApp.serializers import DepartementSerialiser, EmployeesSerialiser
from django.http.response import JsonResponse
from django.core.files.storage import default_storage


@csrf_exempt
def departementApi(request, id=0):
    if request.method == 'GET':
        departements = Departements.objects.all()
        departements_serialiser = DepartementSerialiser(departements, many=True)
        return JsonResponse(departements_serialiser.data, safe=False)
    elif request.method == 'POST':
        departement_data = JSONParser().parse(request)
        departements_serialiser = DepartementSerialiser(data=departement_data)
        if departements_serialiser.is_valid():
            departements_serialiser.save()
            return JsonResponse('Added Successfully !!', safe=False)
        return JsonResponse('Failed to Add!', safe=False)
    elif request.method == 'PUT':
        departement_data = JSONParser().parse(request)
        departement = Departements.objects.get(DepartementId=departement_data['DepartementId'])
        departements_serialiser = DepartementSerialiser(departement, data=departement_data)
        if departements_serialiser.is_valid():
            departements_serialiser.save()
            return JsonResponse('Change Successfully !!', safe=False)
        return JsonResponse('Failed to Add!', safe=False)
    
    elif request.method == 'DELETE':
        departement = Departements.objects.get(DepartementId=id)
        departement.delete()
        return JsonResponse("Deleted Successfully!", safe=False)

@csrf_exempt
def employeeApi(request, id=0):
    if request.method == 'GET':
        employees = Employees.objects.all()
        employees_serialiser = EmployeesSerialiser(employees, many=True)
        return JsonResponse(employees_serialiser.data, safe=False)
    elif request.method == 'POST':
        employee_data = JSONParser().parse(request)
        employees_serialiser = EmployeesSerialiser(data=employee_data)
        if employees_serialiser.is_valid():
            employees_serialiser.save()
            return JsonResponse('Added Successfully !!', safe=False)
        return JsonResponse('Failed to Add!', safe=False)
    elif request.method == 'PUT':
        employee_data = JSONParser().parse(request)
        employees = Employees.objects.get(EmployeeId=employee_data['EmployeeId'])
        employees_serialiser = EmployeesSerialiser(employees, data=employee_data)
        if employees_serialiser.is_valid():
            employees_serialiser.save()
            return JsonResponse('Change Successfully !!', safe=False)
        return JsonResponse('Failed to Add!', safe=False)
    
    elif request.method == 'DELETE':
        employees = Employees.objects.get(EmployeeId=id)
        employees.delete()
        return JsonResponse("Deleted Successfully!", safe=False)
    
@csrf_exempt
def SaveFile(request):
    file = request.FILES['MyFile']
    file_name = default_storage.save(file.name, file)

    return JsonResponse(file_name, safe=False)