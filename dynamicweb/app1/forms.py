from django import forms
from app1.models import Employee, News, Calender

class EmployeeForm(forms.ModelForm):
	class Meta:
		model=Employee
		fields='__all__'


class NewsForm(forms.ModelForm):
	class Meta:
		model=News
		fields='__all__'

class CalenderForm(forms.ModelForm):
	class Meta:
		model=Calender
		fields='__all__'


