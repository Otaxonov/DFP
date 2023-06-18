from django.urls import path
from School import views

urlpatterns = [
    path('', views.StudentsView, name='students_list'),
    path('create/', views.StudentCreateView, name="student_create"),
    path('update/<int:pk>/', views.StudentUpdateView, name="student_update"),
    path('delete/<int:pk>/', views.StudentDeleteView, name="student_delete"),
    path('sign-up/', views.SignUpView, name="sign_up"),
    path('sign-in/', views.SignInView, name="sign_in"),
    path('sign-out/', views.SignOutView, name="sign_out"),
    path('profile/', views.ProfileView, name="profile_update"),
]