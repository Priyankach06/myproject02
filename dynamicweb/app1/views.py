from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from app1.models import Employee, News, Calender
from app1.forms import EmployeeForm, NewsForm, CalenderForm
import csv
from django.http import HttpResponse


def homeview(request):
	return render(request,'app1/home.html')

@login_required
def managerview(request):
	return render(request,'app1/hr.html')

def employeeview(request):
	return render(request,'app1/emp.html')

def addempview(request):
	form = EmployeeForm()
	if request.method=="POST":
		form = EmployeeForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/empdata')
			
	return render(request,'app1/addemp.html',{'form':form})
	
	
def empdataview(request):
	emp=Employee.objects.all()
	return render(request,'app1/empdata.html',{'e':emp})

def newsview(request):
	form = NewsForm()
	if request.method=="POST":
		form = NewsForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/latestnws')		
	return render(request,'app1/news.html',{'form':form})
	

def calview(request):
	form = CalenderForm()
	if request.method=="POST":
		form = CalenderForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/hldy')		
	return render(request,'app1/cal.html',{'form':form})

def deleteview(request,id):
	emp=Employee.objects.get(id=id)
	emp.delete()
	return redirect('/empdata')

def updateview(request,id):
	emp=Employee.objects.get(id=id)
	if request.method=="POST":
		form = EmployeeForm(request.POST, instance=emp)
		if form.is_valid():
			form.save()
			return redirect('/empdata')
	return render(request,'app1/up.html',{'e':emp})
			
def getfile(request):
	response= HttpResponse(content_type='text/csv')
	response['Content-Disposition']='attachment; filename="employeedata.csv"'
	employees= Employee.objects.all()
	writer = csv.writer(response)
	writer.writerow(['Emp Name','Emp ID','Designation','Date of Joining','Department','Salary Package','Experience'])
	for i in employees:
		writer.writerow([i.Empname,i.EmpID,i.Designation,i.DateofJoining,i.Department,i.SalaryPackage,i.Experience])
	return response

def hldyview(request):
	ch=Calender.objects.all()
	return render(request,'app1/hldy.html',{'c':ch})

def latestnwsview(request):
	nws=News.objects.all()
	return render(request,'app1/latestnws.html',{'n':nws})

