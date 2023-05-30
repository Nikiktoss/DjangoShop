from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django import forms
from django.contrib.auth.password_validation import validate_password

from .models import ShopUser


class ShopUserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(ShopUserLoginForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'input__field'
            field.widget.attrs['placeholder'] = f'Input {field_name}'

    class Meta:
        model = ShopUser
        fields = ("username", "password")


class ShopUserRegistrationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(ShopUserRegistrationForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'input__field'
            if field_name != 'password1' and field_name != 'password2':
                field.widget.attrs['placeholder'] = f'input {field_name}'
            else:
                if field_name == 'password1':
                    field.widget.attrs['placeholder'] = 'input password'
                else:
                    field.widget.attrs['placeholder'] = 'confirm password'

    def clean(self):
        password1 = self.cleaned_data['password1']
        validate_password(password=password1)
        return self.cleaned_data

    def clean_username(self):
        username = self.cleaned_data["username"]

        if ShopUser.objects.filter(username=username).exists():
            raise forms.ValidationError("User with such name already exists")

        return username

    def clean_email(self):
        email = self.cleaned_data["email"]

        if ShopUser.objects.filter(email=email).exists():
            raise forms.ValidationError("User with such email already exists")

        return email

    class Meta:
        model = ShopUser
        fields = ("username", "email", "password1", "password2")
