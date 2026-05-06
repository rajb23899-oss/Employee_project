from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register_page,name='register_page'),
    path('add/', views.add_employee,name='add_employee'),
    path('', views.view_employee_details,name='view_employee_details'),
    path('get/<int:id>/', views.get_employee_details,name='get_employee_details'),
    path('delete/<int:id>/', views.delete_employee,name='delete_employee'),
]