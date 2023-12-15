from django.db import models

class Employee(models.Model):
	
	Empname=models.CharField(max_length=50)
	EmpID=models.IntegerField()
	Designation=models.CharField(max_length=50)
	DateofJoining=models.IntegerField()
	Department=models.CharField(max_length=50)
	SalaryPackage=models.IntegerField()
	Experience=models.IntegerField()

class News(models.Model):
	
	Occation=models.CharField(max_length=250)

class Calender(models.Model):

	Date=models.IntegerField()
	Occation=models.CharField(max_length=250)
