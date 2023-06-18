from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth import get_user_model
from django import forms
from School.models import Student

User = get_user_model()

def start_with_s(value):
    if not value[0].isupper():
        raise forms.ValidationError('Name should start with Upper case')


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
        ),
        validators=[start_with_s]
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


    def clean_first_name(self):
        nm = self.cleaned_data['first_name']

        if len(nm) < 4:
            raise forms.ValidationError('Enter more than or equal 4')
        
        return nm
    

def clean(self):
    #cleaned_data = super().clean()

    #nm = self.cleaned_data['first_name']

    #if len(nm) > 10:
    #    raise forms.ValidationError('Enter less than or equal 10')
        
    #return nm
    pass


def validate_username(value):
    # [a-zA-Z0-9]
    pass


class UpdateStudentForm(forms.ModelForm):
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


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


    username = forms.CharField(
        required=True,
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control mb-3',
            }
        )
    )

    email = forms.EmailField(
        required=True,
        max_length=100,
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control mb-3',
            }
        )
    )

    password1 = forms.CharField(
        label="Password",
        required=True,
        max_length=100,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control mb-3',
            }
        )
    )

    password2 = forms.CharField(
        label="Password Confirmation",
        required=True,
        max_length=100,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control mb-3',
            }
        )
    )

class SignInForm(AuthenticationForm):
    class Meta:
        model = User
        fields = "__all__"


    username = forms.CharField(
        required=True,
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control mb-3',
            }
        )
    )

    password = forms.CharField(
        required=True,
        max_length=100,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control mb-3',
            }
        )
    )


class UserUpdateForm(UserChangeForm):
    password = None
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']

    
    username = forms.CharField(
        required=True,
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control mb-3',
            }
        )
    )

    email = forms.EmailField(
        required=True,
        max_length=100,
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control mb-3',
            }
        )
    )

    first_name = forms.CharField(
        required=True,
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control mb-3',
            }
        )
    )

    last_name = forms.CharField(
        required=True,
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control mb-3',
            }
        )
    )