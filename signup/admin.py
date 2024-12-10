from django.contrib import admin
from .models import Profile

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'preferred_language', 'theme', 'notifications_enabled', 'share_data')
    list_filter = ('preferred_language', 'theme', 'notifications_enabled', 'share_data')
    search_fields = ('user__username', 'user__email')