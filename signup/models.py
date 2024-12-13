from django.conf import settings
from django.db import models

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    # Настройка языка
    LANGUAGE_CHOICES = [
        ('ru', 'Русский'),
        ('en', 'English'),
    ]
    preferred_language = models.CharField(max_length=10, choices=LANGUAGE_CHOICES, default='ru')

    # Тема оформления
    THEME_CHOICES = [
        ('As system', 'Как в системе'),
        ('light', 'Светлая'),
        ('dark', 'Тёмная'),
    ]
    theme = models.CharField(max_length=10, choices=THEME_CHOICES, default='light')

    # Настройки отображения каталога
    CONTENT_CHOICES = [
        ('grid', 'Сетка'),
        ('list', 'Лист'),
    ]
    catalog_view = models.CharField(max_length=10, choices=CONTENT_CHOICES, default="grid")

    enable_crazy_settings = models.BooleanField(default=False)

    # Crazy settings
    font_size = models.IntegerField(default=14)  # Размер шрифта
    font_family = models.CharField(max_length=100, default="Arial")  # Гарнитура
    kerning = models.DecimalField(max_digits=4, decimal_places=2, default=1.0)  # Кернинг
    line_spacing = models.DecimalField(max_digits=4, decimal_places=2, default=1.5)  # Интервал
    show_images = models.BooleanField(default=True)  # Показывать изображения

    def __str__(self):
        return f"Profile of {self.user.username}"
    