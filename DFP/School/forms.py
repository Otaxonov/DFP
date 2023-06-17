from django import forms
from School.models import Student

class CreateStudentForm(forms.ModelForm):

    class Meta:
        model = Student
        fields = '__all__'

    first_name = forms.CharField(
        required=True,
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control mb-3',
                'placeholder': 'Type Your Name...'
            }
        )
    )

    last_name = forms.CharField(
        required=True,
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control mb-3',
                'placeholder': 'Type Your Surname...'
            }
        )
    )

    birthday = forms.DateField(
        required=True,
        widget=forms.DateInput(
            attrs={
                'class': 'form-control mb-3',
                'value': '2020-01-01'
            }
        )
    )
