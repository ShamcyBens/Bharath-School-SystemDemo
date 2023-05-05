
from django import forms
from .models import Student

class DeleteStudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = []


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ('name', 'age', 'grade')