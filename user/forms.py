from django import forms
from django.contrib.auth.models import User


class RegisterUserForm(forms.ModelForm):
    """
    Register new users.
    Includes fields for username, first name, email address, and password.
    """
    username = forms.CharField(max_length=150, required=True)
    first_name = forms.CharField(
        max_length=52, required=True, help_text="Maximum 50 characters."
    )
    email = forms.EmailField(required=True, help_text='Enter your email address')
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput)
    password2 = forms.CharField(
        label="Password confirmation", widget=forms.PasswordInput
    )

    class Meta:
        model = User
        fields = ('username','first_name', 'email', 'password1', 'password2')

    def clean_password2(self):
        """
        Validate that the two password entries match.
        """
        password1 = self.cleaned_data('password1')
        password2 = self.cleaned_data('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Password don't match")
        return password2


    def save(self, commit=True):
        user = super(RegisterUserForm, self).save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.email = self.cleaned_data['email']
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user
    