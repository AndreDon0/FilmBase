from django import forms
from django.contrib.auth import get_user_model
from .models import Profile

User = get_user_model()


class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']
        labels = {
            'first_name': 'Имя',
            'last_name': 'Фамилия',
            'email': 'Электронная почта',
        }


class ProfileSettingsForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['preferred_language', 'theme', 'catalog_view', 'enable_crazy_settings']
        labels = {
            'preferred_language': 'Предпочитаемый язык',
            'theme': 'Тема сайта',
            'catalog_view': 'Отображение каталога',
            'enable_crazy_settings': 'Включить безумные настройки',
        }


class CrazySettingsForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['font_size', 'font_family', 'kerning', 'line_spacing', 'show_images']
        labels = {
            'font_size': 'Размер шрифта',
            'font_family': 'Шрифт',
            'kerning': 'Кернинг',
            'line_spacing': 'Интервал',
            'show_images': 'Изображения',
        }
