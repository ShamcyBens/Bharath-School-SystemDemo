from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Student
from .forms import StudentForm

def home(request):
    students = Student.objects.all()
    return render(request, 'test/home.html', {'students': students})

def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = StudentForm()
    return render(request, 'test/student_form.html', {'form': form})

def delete_student(request, pk):
    student = Student.objects.get(id=pk)
    if request.method == 'POST':
        student.delete()
        return redirect('home')
    return render(request, 'test/delete_student_confirm.html', {'student': student})
