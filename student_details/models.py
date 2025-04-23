from django.db import models
from datetime import date
class Student(models.Model):

    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    roll_number = models.CharField(max_length=20,unique=True)
    dept = models.CharField(max_length=20)
    email = models.EmailField()
    phone_number = models.IntegerField(max_length=10)
    dob = models.DateField(default=date(2000,1,1))
    address = models.TextField(max_length=1000,blank=True)
    
    def __str__(self):
        return self.firstname


