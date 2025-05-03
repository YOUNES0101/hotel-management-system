from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class UserLoginForm(forms.Form):
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={'class': 'auth-form__input', 'placeholder': 'Your email'})
    )
    password = forms.CharField(
        required=True,
        widget=forms.PasswordInput(attrs={'class': 'auth-form__input', 'placeholder': 'Your password'})
    )
    remember = forms.BooleanField(required=False)

class UserRegistrationForm(forms.ModelForm):
    name = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={'class': 'auth-form__input', 'placeholder': 'Your full name'})
    )
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={'class': 'auth-form__input', 'placeholder': 'Your email'})
    )
    password = forms.CharField(
        required=True,
        widget=forms.PasswordInput(attrs={'class': 'auth-form__input', 'placeholder': 'Create a password'}),
        validators=[validate_password]
    )
    password_confirmation = forms.CharField(
        required=True,
        widget=forms.PasswordInput(attrs={'class': 'auth-form__input', 'placeholder': 'Confirm your password'})
    )

    class Meta:
        model = CustomUser
        fields = ('email',)

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if CustomUser.objects.filter(email=email).exists():
            raise ValidationError("A user with this email already exists.")
        return email

    def clean_password_confirmation(self):
        password = self.cleaned_data.get("password")
        password_confirmation = self.cleaned_data.get("password_confirmation")
        if password and password_confirmation and password != password_confirmation:
            raise ValidationError("The passwords do not match.")
        return password_confirmation

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']

        # Set first_name and last_name from the full name
        if 'name' in self.cleaned_data and self.cleaned_data['name']:
            name_parts = self.cleaned_data['name'].split(' ', 1)
            user.first_name = name_parts[0]
            if len(name_parts) > 1:
                user.last_name = name_parts[1]

        if commit:
            user.save()
        return user

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email Address'})
    )
    password1 = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}),
        help_text="Your password must be at least 8 characters long and contain a mix of letters, numbers, and symbols."
    )

    password2 = forms.CharField(
        label='Confirm Password',
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirm Password'}),
        help_text="Enter the same password as above, for verification."
    )
    # Add custom validation for password strength
    def clean_password1(self):
        password = self.cleaned_data.get('password1')
        try:
            validate_password(password)
        except ValidationError as e:
            raise forms.ValidationError(e.messages)
        return password


    class Meta:
        model = CustomUser
        fields = ['email', 'password1', 'password2']


    def clean_email(self):
        email = self.cleaned_data.get('email')
        if CustomUser.objects.filter(email=email).exists():
            raise forms.ValidationError("A user with this email already exists.")
        return email

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Remove help_text from password fields

        self.fields['password2'].help_text = None


    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user



