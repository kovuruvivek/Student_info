from django.shortcuts import render,redirect
from .forms import CreateStudentForm
from .models import Student
from django.shortcuts import get_object_or_404

def student_form(request):
    form = CreateStudentForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('thank_you')
    return render(request,'student_form.html',{'form':form})

def thank_you(request):
    return render(request,'Thank_You.html')

def student_list(request):
    Stu = Student.objects.all().order_by('firstname')
    return render(request,'Student_list.html',{'Stu':Stu})


def edit_details(request,sedit_id):
    s = get_object_or_404(Student,id=sedit_id)
    form = CreateStudentForm(request.POST or None, instance = s)
    if form.is_valid():
        form.save()
        return redirect('student_list')
    return render(request,'Edit_student.html',{'form':form})
    
def delete_details(request,sdel_id):
    d = get_object_or_404(Student,id = sdel_id)
    if request.method == 'POST':
        d.delete()
        return redirect('student_list')
    return render(request,'Student_delete.html',{'d':d})

def home(request):
    return render(request,'home.html')