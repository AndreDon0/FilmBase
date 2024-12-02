from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import UserUpdateForm

@login_required
def settings_view(request):
    if request.method == 'POST':
        form = UserUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('settings')  # Перенаправляем пользователя обратно на страницу настроек
    else:
        form = UserUpdateForm(instance=request.user)
    
    return render(request, 'settings/settings.html', {'form': form})