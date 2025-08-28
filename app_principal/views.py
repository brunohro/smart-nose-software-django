from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from .models import LeituraSensor
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

def sensores(request):
    sensors = LeituraSensor.objects.all()
    return render(request, 'sensores.html', {'sensors': sensors})



# def index(request):
#     produtos = Produto.objects.all()
#     categoria = Categoria.objects.all()

#     if request.method == 'POST':
#         query_pesquisa = request.POST.get("search", None)
#         if query_pesquisa is not None:
#             produtos = produtos.filter(nome__icontains=query_pesquisa)

#     return render(request, 'index.html', {'produtos': produtos, 'categorias': categoria})