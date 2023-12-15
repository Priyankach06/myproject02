
from django.contrib import admin
from django.urls import path, include
from app1 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.homeview),
	path('hr/', views.managerview),
	path('emp/', views.employeeview),
	path('accounts/',include('django.contrib.auth.urls')),
    path('addemp/', views.addempview),
    path('empdata/', views.empdataview),
    path('news/', views.newsview),
    path('cal/', views.calview),
    path('delete/<int:id>', views.deleteview),
    path('update/<int:id>', views.updateview),
    path('data/', views.getfile),
    path('hldy/', views.hldyview),
    path('latestnws/', views.latestnwsview),
    
    
   




]