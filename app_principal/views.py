from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from .models import LeituraSensor
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.forms import UserCreationForm
from django.db.models import Q
from django.contrib import messages

def index(request):
    return redirect('login')

@login_required
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

@login_required
def sensores(request):
    sensors = LeituraSensor.objects.all()
    return render(request, 'sensores.html', {'sensors': sensors})

@login_required
def temperatura(request):
    return render(request, 'temperatura.html')


def mostrar_usuario(request, id):
    usuario = User.objects.get(id=id)
    return render(request, 'user/mostrar_usuario.html', {'usuario': usuario})

def gerir_usuarios(request):
    search_query = request.GET.get('search', '')
    if search_query:
        users = User.objects.filter(
            Q(username__icontains=search_query) |
            Q(email__icontains=search_query)
        ).order_by('username')
    else:
        users = User.objects.all().order_by('username')

    context = {
        'users': users,
        'search_query': search_query,
    }

    return render(request, 'user/admin/gerir_usuarios.html', context)

def cadastrar_usuarios(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            # Define se é admin
            user.is_staff = request.POST.get('is_staff') == 'True'
            user.save()
            messages.success(request, f'Usuário {user.username} criado com sucesso!')
            return redirect('criar_usuario')
    else:
        form = UserCreationForm()
    
    return render(request, 'user/admin/cadastrar_usuario.html', {
        'form': form,
        'errors': form.errors,
        'success_on_insert': messages.get_messages(request),
    })