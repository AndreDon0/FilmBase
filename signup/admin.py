from django.contrib import admin
from .models import Profile

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'preferred_language', 'theme', 'catalog_view')
    list_filter = ('preferred_language', 'theme', 'catalog_view')
    search_fields = ('user__username', 'user__email')