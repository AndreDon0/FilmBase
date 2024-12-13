from django import forms
from django.contrib.auth import get_user_model
from .models import Profile

User = get_user_model()

class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']

class ProfileSettingsForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['preferred_language', 'theme', 'catalog_view', 'enable_crazy_settings']

class CrazySettingsForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['font_size', 'font_family', 'kerning', 'line_spacing', 'show_images']