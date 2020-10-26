from django import forms
from django.contrib.auth import get_user_model

# Check for unique email and username

User = get_user_model()

class RegisterForm(forms.Form):
    username = forms.CharField()
    email = forms.EmailField()
    password1 = forms.CharField(
        # Hides password while typing
        label='Password',
        widget=forms.PasswordInput(
            # Set HTML attributes
            attrs={
                "class": "form-control",
                "id": "user-password"
            }
        )
    )

    password2 = forms.CharField(
        # Hides password while typing
        label='Confirm Password',
        widget=forms.PasswordInput(
            # Set HTML attributes
            attrs={
                "class": "form-control",
                "id": "user-confirm-password"
            }
        )
    )

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(
        # Hides password while typing
        widget=forms.PasswordInput(
            # Set HTML attributes
            attrs={
                "class": "form-control",
                "id": "user-password"
            }
        )
    )

    def clean_username(self):
        username = self.cleaned_data.get('username')
        qs = User.objects.filter(username__iexact=username)
        if qs.exists():
            raise forms.ValidationError("This is an invalid username, please pick another.")

        return username
        
        
    def clean_email(self):
        email = self.cleaned_data.get('email')
        qs = User.objects.filter(username__iexact=email)
        if qs.exists():
            raise forms.ValidationError("This email is already in use.")

        return email