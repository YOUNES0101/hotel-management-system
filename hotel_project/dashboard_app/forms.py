from django import forms
from hotel_app.models import CustomUser
from django.contrib.auth.forms import UserCreationForm

class CustomUserForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = CustomUser
        fields = ( "email","is_superuser" ,"password1", "password2")
        widgets = {
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email Address'}),
            'Superuser': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirm Password'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Remove help_text from password fields
        self.fields['password1'].help_text = None
        self.fields['password2'].help_text = None


    def clean_email(self):
        email = self.cleaned_data.get('email')
        if CustomUser.objects.filter(email=email).exists():
            raise forms.ValidationError("A user with this email already exists.")
        return email


    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if self.cleaned_data.get('is_staff'):
            user.is_superuser = True
        if commit:
            user.save()
        return user





