from cProfile import label

from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm



class RegistrationForm(UserCreationForm):
    username = forms.CharField(label="Логин", error_messages={
                               "required": "Введите логин"
                                })
    first_name = forms.CharField(label="Имя")
    last_name = forms.CharField(label="Фамилия")
    email = forms.EmailField(label="Эл. почта")
    password1 = forms.CharField(label="Введите пароль",
                               widget=forms.PasswordInput)
    password2 = forms.CharField(label="Подтвердите пароль",
                                widget=forms.PasswordInput, error_messages={
                               "required": "Потвердите пароль"
                                })


    class Meta:
        model = User
        fields = ("username", "first_name", "last_name", "email", "password1", "password2")

class NewRegistrationForm(forms.ModelForm):
    class Meta:
        password2 = forms.CharField(label="Подтвердите пароль",
                                    widget=forms.PasswordInput)
        model = User
        fields = ("username", "first_name", "last_name", "email", "password")

        help_texts = {
            "username": ""
        }

    def clean_password2(self):
        cleaned_data = self.cleaned_data
        if cleaned_data['password'] != cleaned_data['password2']:
            raise forms.ValidationError("Пароли не совпадают")
        return cleaned_data['password2']