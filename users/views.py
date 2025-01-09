from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import CustomUserCreationForm


def login_view(request):
    error_message = None
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            error_message = "Błędne dane logowania."

    return render(request, 'users/login.html', {'error': error_message})


def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
    else:
        form = CustomUserCreationForm()
    for field in form:
        field.field.widget.attrs.update({'placeholder': f'{field.label}'})
    return render(request, 'users/register.html', {'form': form})

def logout_view(request):
    logout(request)  # Funkcja z django.contrib.auth wylogowująca usera
    return redirect('index')  # lub inna nazwa ścieżki/URL

