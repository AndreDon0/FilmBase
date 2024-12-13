from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserEditForm, ProfileSettingsForm, CrazySettingsForm
from django.utils.translation import activate

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('films:home')
    else:
        form = UserCreationForm()
    return render(request, "signup/signup.html", {'form': form})


@login_required
def edit_profile(request):
    profile = request.user.profile

    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user, data=request.POST)
        settings_form = ProfileSettingsForm(instance=profile, data=request.POST)
        crazy_settings_form = CrazySettingsForm(instance=profile, data=request.POST)

        if user_form.is_valid() and settings_form.is_valid() and crazy_settings_form.is_valid():
            user_form.save()
            settings_form.save()
            crazy_settings_form.save()

            activate(profile.preferred_language)

            messages.success(request, "Настройки успешно сохранены.")
            return redirect('signup:settings')
    else:
        user_form = UserEditForm(instance=request.user)
        settings_form = ProfileSettingsForm(instance=profile)
        crazy_settings_form = CrazySettingsForm(instance=profile)

    return render(request, 'signup/settings.html', {
        'user_form': user_form,
        'settings': settings_form,
        'crazy_settings': crazy_settings_form,
    })