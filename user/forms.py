from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegisterUserForm(UserCreationForm):
    """
    Register new users.
    Includes fields for username, first name, email address, and password.
    """
    first_name = forms.CharField(
        max_length=52, required=True, help_text="Maximum 50 characters."
    )
    email = forms.EmailField(required=True, help_text='Enter your email address')

    class Meta:
        model = User
        fields = ('username','first_name', 'email', 'password1', 'password2')

    def save(self, commit=True):
        user = super(RegisterUserForm, self).save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user