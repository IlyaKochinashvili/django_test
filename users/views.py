from django.contrib.auth import login
from django.shortcuts import redirect, render

from users.forms import UserForm


def signup(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user, backend="django.contrib.auth.backends.ModelBackend")
            return redirect('/')
    else:
        form = UserForm()
    return render(request, 'registration/signup.html', {'form': form})
