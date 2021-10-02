from django import forms
from .models import Account
from django.forms import ModelForm


class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Enter your password',
        'class': 'form-control',
    }))
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Confirm your password'
    }))
    class Meta:
        model = Account
        fields = ['first_name', 'last_name', 'phone_number', 'email', 'password']



    def clean(self):
        cleaned_data = super(RegistrationForm, self).clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password != confirm_password:
            raise forms.ValidationError(
                "password does not match"
            )

    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs['placeholder'] = 'Enter First Name'
        self.fields['last_name'].widget.attrs['placeholder'] = 'Enter Last Name'
        self.fields['email'].widget.attrs['placeholder'] = 'Enter Your Email'
        self.fields['phone_number'].widget.attrs['placeholder'] = 'Enter Your Phone Number'
        self.fields['password'].widget.attrs['placeholder'] = 'Enter Your Password'
        self.fields['confirm_password'].widget.attrs['placeholder'] = 'Renter Your Password'
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'