from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.Employeeshow.as_view()),
    path('emp/<int:eid>',views.EmployeeUpdate.as_view())

]
