from django.shortcuts import render, redirect
from School.models import Student
from School.forms import CreateStudentForm

# Create your views here.

def StudentsView(request):

    students = Student.objects.all()

    context = {
        'title': "School Management App",
        "students": students
    }

    return render(request, 'school/students.html', context=context)

def StudentCreateView(request):
    if request.method == 'POST':
        form = CreateStudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('students_list')
    else:
        form = CreateStudentForm()

    context = {
        'title': "Create Student",
        'form': form
    }

    return render(request, 'school/create.html', context=context)
