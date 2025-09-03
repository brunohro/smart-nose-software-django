from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from .models import LeituraSensor #, Usuario
from django.contrib.auth.decorators import login_required
# from .forms import UsuarioForm

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


# def cadastrar_usuario(request):
#     if request.method == 'POST':
#         form = UsuarioForm(request.POST)
#         if form.is_valid():
#             user = form.save() 
#             user.set_password(form.cleaned_data['password'])
#             user.save()
#             return redirect('login')
#     else:
#         form = UsuarioForm()
#     return render(request, 'usuarios/cadastrar_usuario.html', {'form': form})

# def editar_usuario(request, id):
#     usuario = get_object_or_404(usuario, id=id)
#     usuario = usuario.objects.get(id=id)
#     if request.method == 'POST':
#         form = usuarioForm(request.POST, instance=usuario)
#         if form.is_valid():
#             user = form.save() 
#             user.set_password(form.cleaned_data['password'])
#             user.save()
#             return redirect('index')
#     else:
#         form = usuarioForm(instance=usuario)
#     return render(request, 'usuarios/cadastrar_usuario.html', {'form': form})

# def remover_usuario(request, id):
#     usuario = get_object_or_404(usuario, id=id)
#     usuario = usuario.objects.get(id=id)
#     usuario.delete() 
#     return redirect('administrador')
#     #return render(request, 'usuarios/remover_usuario.html', {'usuario': usuario})  # Exibe confirmação para remover
