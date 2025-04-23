from django import forms
from .models import Student

class CreateStudentForm(forms.ModelForm):
    
    class Meta:
        model = Student
        fields = ['firstname','lastname','roll_number','dept','email','phone_number','dob','address']

