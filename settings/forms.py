from django import forms
from django.contrib.auth.models import User

class UserUpdateForm(forms.ModelForm):
    first_name = forms.CharField(label="Имя", max_length=30, required=True)
    last_name = forms.CharField(label="Фамилия", max_length=30, required=True)
    email = forms.EmailField(label="Адрес электронной почты", required=True)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']