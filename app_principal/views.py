from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User

def dashboard(request):
    return render(request, 'dashboard.html')


def login_view(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")

        user = authenticate(request, username=email, password=password)

        if user is not None:
            login(request, user)
            return redirect("dashboard")
        else:
            messages.error(request, "Email ou senha inválidos")
    return render(request, "login.html", {"project_name": "E-nose"})


def logout_view(request):
    logout(request)
    return redirect("login")

# primary key do user
def user_detail(request, pk):
    user_obj = get_object_or_404(User, pk=pk)
    context = {
        'user_obj': user_obj,
    }
    return render(request, 'dashboard.html', context)
