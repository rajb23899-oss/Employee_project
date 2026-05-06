from django.db import models

# Create your models here.
class Employee(models.Model):
    e_name = models.CharField(max_length=100)
    e_number = models.IntegerField()
    e_email = models.EmailField()
    e_salary = models.FloatField()
    e_company = models.CharField(max_length=100)
    e_image = models.ImageField(upload_to='employees/')
    
    
    def __str__(self):
        return self.e_name
    
