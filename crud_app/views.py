from django.shortcuts import render
from .serializers import EmployeeSerialize
from .models import Employee
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
# Create your views here.
class Employeeshow(APIView):
    def get(self,request):
        emp=Employee.objects.all()
        serobj=EmployeeSerialize(emp,many=True)
        return Response(serobj.data)
    def post(self,request):
        emps=EmployeeSerialize(data=request.data)
        if emps.is_valid():
           emps.save()
           return Response(emps.data,status.HTTP_201_CREATED)
        return Response(status.HTTP_400_BAD_REQUEST)
class EmployeeUpdate(APIView):
    def get(self,request,eid):
        empo=Employee.objects.get(id=eid)
        emps=EmployeeSerialize(empo)
        return Response(emps.data)
    def put(self,request,eid):
        empo = Employee.objects.get(id=eid)
        emps = EmployeeSerialize(empo,data=request.data)
        if emps.is_valid():
            emps.save()
            return Response(emps.data,status.HTTP_201_CREATED)
        return Response(emps.errors,status.HTTP_400_BAD_REQUEST)
    def delete(self,request,eid):
        empoject=Employee.objects.get(id=eid)
        empoject.delete()
        return Response(status.HTTP_200_OK)