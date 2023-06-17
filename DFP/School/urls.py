from django.urls import path
from School import views

urlpatterns = [
    path('', views.StudentsView, name='students_list'),
    path('create/', views.StudentCreateView, name="student_create")
]