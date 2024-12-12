from django.urls import path
from . import views

app_name = "signup"
urlpatterns = [
    path('', views.signup, name='signup'),
    path('settings/', views.edit_profile, name='settings'),
]
