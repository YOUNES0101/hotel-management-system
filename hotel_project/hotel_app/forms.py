from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from .models import CustomUser


# class CustomUserCreationForm(UserCreationForm):
#     email = forms.EmailField(
#         required=True,
#         widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email Address'})
#     )

#     class Meta:
#         model = User
#         fields = ['username', 'email', 'password1', 'password2']

#     def save(self, commit=True):
#         user = super().save(commit=False)
#         user.email = self.cleaned_data['email']
#         if commit:
#             user.save()
#         return user
# class CustomUserCreationForm(UserCreationForm):
#     email = forms.EmailField(
#         required=True,
#         widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email Address'})
#     )

#     class Meta:
#         model = User
#         fields = ['email', 'password1', 'password2']

#     def clean_email(self):
#         email = self.cleaned_data.get('email')
#         if User.objects.filter(email=email).exists():
#             raise forms.ValidationError("A user with this email already exists.")
#         return email

#     def save(self, commit=True):
#         user = super().save(commit=False)
#         user.username = self.cleaned_data['email']
#         user.email = self.cleaned_data['email']
#         if commit:
#             user.save()
#         return user

from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email Address'})
    )

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
        self.fields['password1'].help_text = None
        self.fields['password2'].help_text = None


    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user