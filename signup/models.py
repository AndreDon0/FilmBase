from django.conf import settings
from django.db import models

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    
    LANGUAGE_CHOICES = [
        ('ru', 'Русский'),
        ('en', 'English'),
    ]
    THEME_CHOICES = [
        ('light', 'Светлая'),
        ('dark', 'Тёмная'),
    ]

    preferred_language = models.CharField(max_length=5, choices=LANGUAGE_CHOICES, default='ru')
    theme = models.CharField(max_length=5, choices=THEME_CHOICES, default='light')
    notifications_enabled = models.BooleanField(default=True)
    share_data = models.BooleanField(default=True)

    def __str__(self):
        return f"Profile of {self.user.username}"
