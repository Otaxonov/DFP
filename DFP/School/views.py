from django.shortcuts import render, redirect
from School.models import Student
from School.forms import CreateStudentForm, UpdateStudentForm, SignUpForm, SignInForm, UserUpdateForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your views here.

def StudentsView(request):

    students = Student.objects.all()

    context = {
        'title': "School Management App",
        "students": students
    }

    return render(request, 'school/students.html', context=context)

@login_required
def StudentCreateView(request):
    if request.method == 'POST':
        form = CreateStudentForm(request.POST)
        if form.is_valid():
            form.save()

            messages.success(request, f'Student created successfully', extra_tags='success')
            return redirect('students_list')
    else:
        form = CreateStudentForm()

    context = {
        'title': "Create Student",
        'form': form
    }

    return render(request, 'school/create.html', context=context)

@login_required
def StudentUpdateView(request, pk):
    student = Student.objects.get(pk=pk)

    if request.method == 'POST':
        form = UpdateStudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()

            messages.success(request, f'Student updated successfully', extra_tags='success')
            return redirect('students_list')
    else:
        form = UpdateStudentForm(instance=student)

    context = {
        'title': "Update Student",
        'form': form,
        'student': student
    }

    return render(request, 'school/update.html', context=context)

@login_required
def StudentDeleteView(request, pk):
    student = Student.objects.get(pk=pk)
    student.delete()

    messages.warning(request, f'Student deleted successfully', extra_tags='danger')
    return redirect('students_list')

def SignUpView(request):
    
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()

            messages.success(request, f'User created successfully', extra_tags='success')
            return redirect('students_list')
    else:
        form = SignUpForm()
    
    context = {
        'title': "Sign Up",
        'form': form
    }

    return render(request, 'school/sign_up.html', context)

def SignInView(request):
    if request.method == "POST":
        form = SignInForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('students_list')
    else:
        form = SignInForm()

    context = {
        'title': "Sign In",
        'form': form
    }

    return render(request, 'school/sign_in.html', context)

@login_required
def SignOutView(request):
    logout(request)
    return redirect('sign_in')


@login_required
def ProfileView(request):

    profile = User.objects.get(pk=request.user.pk)

    if request.method == 'POST':
        form = UserUpdateForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, f'Profile updated successfully', extra_tags='success')
            return redirect('profile_update')
    else:
        form = UserUpdateForm(instance=profile)

    context = {
        "title": "Profile Update",
        "form": form
    }

    return render(request, 'school/profile.html', context)

def ChangePassword(request):
    pass
