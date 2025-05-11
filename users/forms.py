"""Form for user management."""
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

User = get_user_model()

class UserRegistrationForm(UserCreationForm):
    password1 = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'email',
            'username',
            'phone_number'
            ]
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # TODO: Toggle help text on focus onto password input fields
        self.fields['password1'].help_text = ''
        self.fields['password2'].help_text = ''

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get('password1')
        password2 = cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError('Password do not match.')
        
        return cleaned_data

# TODO: Add login form
class LoginForm(forms.Form):
    email = forms.CharField(
        widget = forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter your Email',
        }), 
        label="Email", 
        max_length=255
    )
    
    password = forms.CharField(
        widget = forms.PasswordInput(attrs = {
            'class': 'form-control',
            'placeholder': 'Enter your password',
        }),
        label = "Password"
    )

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        password = cleaned_data.get('password')

        if not email or not password:
            raise forms.ValidationError('Both email and password are required.')
        
        return cleaned_data