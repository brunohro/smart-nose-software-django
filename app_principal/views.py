import json
from django.utils import timezone
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from .models import LeituraSensor, TipoSensor, Experimento
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.forms import UserCreationForm
from django.db.models import Q
from django.contrib import messages
from .forms import FormularioCriacaoUsuario, FormularioCriacaoSensor
#api
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import TipoSensorSerializer, LeituraSensorSerializer
#csv
import csv
from django.http import HttpResponse

class TipoSensorViewSet(viewsets.ModelViewSet):
    queryset = TipoSensor.objects.all()
    serializer_class = TipoSensorSerializer

class LeituraSensorViewSet(viewsets.ModelViewSet):
    queryset = LeituraSensor.objects.all()
    serializer_class = LeituraSensorSerializer

@api_view(['POST'])
def receber_dados(request):
    leituras = request.data.get('leituras', [])

    experimento_ativo = Experimento.objects.filter(ativo=True).first()

    for leitura in leituras:
        nome_sensor = leitura.get('sensor')
        valor = leitura.get('valor')

        try:
            tipo_sensor = TipoSensor.objects.get(nome=nome_sensor)
            
            LeituraSensor.objects.create(
                tipo_sensor=tipo_sensor,
                valor_percentual=valor,
                experimento=experimento_ativo
            )
        except TipoSensor.DoesNotExist:
            print(f"Sensor não encontrado: {nome_sensor}")
            continue

    return Response(
        {"status": "ok", "mensagem": "Leituras registradas com sucesso!"},
        status=status.HTTP_201_CREATED
    )

def index(request):
    return redirect('login')

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

def user_detail(request, pk):
    user_obj = get_object_or_404(User, pk=pk)
    context = {
        'user_obj': user_obj,
    }
    return render(request, 'dashboard.html', context)

@login_required
def dashboard(request):
    experimento_ativo = Experimento.objects.filter(data_fim__isnull=True).first()
    
    if experimento_ativo:
        sensores = LeituraSensor.objects.select_related("tipo_sensor").filter(experimento=experimento_ativo).order_by("data_leitura")
    else:
        sensores = LeituraSensor.objects.select_related("tipo_sensor").order_by("data_leitura")
    
    mq2_data = [s.valor_percentual for s in sensores if s.tipo_sensor.nome == "MQ2"]
    mq3_data = [s.valor_percentual for s in sensores if s.tipo_sensor.nome == "MQ3"]
    mq4_data = [s.valor_percentual for s in sensores if s.tipo_sensor.nome == "MQ4"]
    mq5_data = [s.valor_percentual for s in sensores if s.tipo_sensor.nome == "MQ5"]
    mq6_data = [s.valor_percentual for s in sensores if s.tipo_sensor.nome == "MQ6"]
    mq7_data = [s.valor_percentual for s in sensores if s.tipo_sensor.nome == "MQ7"]
    mq8_data = [s.valor_percentual for s in sensores if s.tipo_sensor.nome == "MQ8"]
    mq9_data = [s.valor_percentual for s in sensores if s.tipo_sensor.nome == "MQ9"]
    mq135_data = [s.valor_percentual for s in sensores if s.tipo_sensor.nome == "MQ135"]
    temperatura_data = [s.valor_percentual for s in sensores if s.tipo_sensor.nome == "TEMPERATURA"]
    umidade_data = [s.valor_percentual for s in sensores if s.tipo_sensor.nome == "UMIDADE"]

    # Eixo X (datas/horários) → aqui você pode pegar só as MQ2, por exemplo, se todas têm mesma frequência
    timestamps = [s.data_leitura.strftime("%H:%M") for s in sensores if s.tipo_sensor.nome == "MQ2"]

    context = {
        "mq2_data": mq2_data,
        "mq3_data": mq3_data,
        "mq4_data": mq4_data,
        "mq5_data": mq5_data,
        "mq6_data": mq6_data,
        "mq7_data": mq7_data,
        "mq8_data": mq8_data,
        "mq9_data": mq9_data,
        "mq135_data": mq135_data,
        "temperatura_data": temperatura_data,
        "umidade_data": umidade_data,
        "timestamps": timestamps,
        "experimento_ativo": experimento_ativo,
    }
    return render(request, 'dashboard.html', context)

#experimento
def iniciar_experimento(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        descricao = request.POST.get('descricao', '')
        Experimento.objects.create(nome=nome, descricao=descricao, ativo=True)
        Experimento.objects.filter(ativo=True).exclude(nome=nome).update(ativo=False)
    return redirect('dashboard')

def encerrar_experimento(request, id):
    exp = Experimento.objects.get(id=id)
    exp.ativo = False
    exp.data_fim = timezone.now()
    exp.save()
    return redirect('dashboard')

def exportar_experimento_csv(request, id):
    exp = Experimento.objects.get(id=id)
    leituras = (
        LeituraSensor.objects
        .filter(experimento=exp)
        .select_related('tipo_sensor')
        .order_by('data_leitura')
    )
    sensores = sorted(list(
        set(leituras.values_list('tipo_sensor__nome', flat=True))
    ))

    leituras_agrupadas = {}

    for leitura in leituras:
        data = leitura.data_leitura.strftime('%d/%m/%Y')
        hora = leitura.data_leitura.strftime('%H:%M:%S')
        chave = (data, hora)
        if chave not in leituras_agrupadas:
            leituras_agrupadas[chave] = {sensor: "" for sensor in sensores}
            leituras_agrupadas[chave]["Data"] = data
            leituras_agrupadas[chave]["Hora"] = hora
        leituras_agrupadas[chave][leitura.tipo_sensor.nome] = leitura.valor_percentual
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = f'attachment; filename="{exp.nome}_{exp.data_inicio.date()}.csv"'

    writer = csv.writer(response)

    writer.writerow(["Data", "Hora"] + sensores)
    for (data, hora) in sorted(leituras_agrupadas.keys()):
        valores = leituras_agrupadas[(data, hora)]
        linha = [valores.get("Data"), valores.get("Hora")] + [valores.get(sensor, "") for sensor in sensores]
        writer.writerow(linha)

    return response

def listar_experimento(request):
    experimentos = Experimento.objects.all()
    return render(request, "experimento.html", {'experimentos': experimentos})

def remover_experimento(request, id):
    experimento = Experimento.objects.get(id=id)
    experimento.delete()
    return redirect('listar_experimento')


#crud sensores
def cadastrar_sensor(request):
    if request.method == "POST":
        form = FormularioCriacaoSensor(request.POST)
        if form.is_valid():
            form.save()
            return redirect('painel_adm')
    else:
        form = FormularioCriacaoSensor()
    
    return render(request, 'user/admin/cadastrar_sensor.html', {'form': form})

@login_required
def sensores(request):
    # Busca todas as leituras em ordem cronológica
    sensores = LeituraSensor.objects.select_related("tipo_sensor").order_by("data_leitura")
    
    mq2_data = [s.valor_percentual for s in sensores if s.tipo_sensor.nome == "MQ2"]
    mq3_data = [s.valor_percentual for s in sensores if s.tipo_sensor.nome == "MQ3"]
    mq4_data = [s.valor_percentual for s in sensores if s.tipo_sensor.nome == "MQ4"]
    mq5_data = [s.valor_percentual for s in sensores if s.tipo_sensor.nome == "MQ5"]
    mq6_data = [s.valor_percentual for s in sensores if s.tipo_sensor.nome == "MQ6"]
    mq7_data = [s.valor_percentual for s in sensores if s.tipo_sensor.nome == "MQ7"]
    mq8_data = [s.valor_percentual for s in sensores if s.tipo_sensor.nome == "MQ8"]
    mq9_data = [s.valor_percentual for s in sensores if s.tipo_sensor.nome == "MQ9"]
    mq135_data = [s.valor_percentual for s in sensores if s.tipo_sensor.nome == "MQ135"]

    # Eixo X (datas/horários) → aqui você pode pegar só as MQ2, por exemplo, se todas têm mesma frequência
    timestamps = [s.data_leitura.strftime("%H:%M") for s in sensores if s.tipo_sensor.nome == "MQ2"]

    context = {
        "mq2_data": mq2_data,
        "mq3_data": mq3_data,
        "mq4_data": mq4_data,
        "mq5_data": mq5_data,
        "mq6_data": mq6_data,
        "mq7_data": mq7_data,
        "mq8_data": mq8_data,
        "mq9_data": mq9_data,
        "mq135_data": mq135_data,
        "timestamps": timestamps,
    }
    return render(request, "sensores.html", context)

def ultima_leitura(request):
    sensores_atuais = {}
    tipos = ["MQ2", "MQ3", "MQ5", "MQ135", "TEMPERATURA", "UMIDADE"]

    for tipo in tipos:
        leitura = (
            LeituraSensor.objects
            .select_related("tipo_sensor")
            .filter(tipo_sensor__nome=tipo)
            .order_by("-data_leitura")
            .first()
        )
        sensores_atuais[tipo] = leitura
    
    # 🔧 Função para formatar com ponto decimal
    def format_number(value):
        return f"{value:.1f}".replace(",", ".") if value is not None else None

    context = {
        "mq2_data": json.dumps([sensores_atuais["MQ2"].valor_percentual]) if sensores_atuais["MQ2"] else "[]",
        "mq3_data": json.dumps([sensores_atuais["MQ3"].valor_percentual]) if sensores_atuais["MQ3"] else "[]",
        "mq5_data": json.dumps([sensores_atuais["MQ5"].valor_percentual]) if sensores_atuais["MQ5"] else "[]",
        "mq135_data": json.dumps([sensores_atuais["MQ135"].valor_percentual]) if sensores_atuais["MQ135"] else "[]",
        "temperatura_data": format_number(sensores_atuais["TEMPERATURA"].valor_percentual) if sensores_atuais["TEMPERATURA"] else None,
        "umidade_data": format_number(sensores_atuais["UMIDADE"].valor_percentual) if sensores_atuais["UMIDADE"] else None,
        "timestamps": json.dumps([
            sensores_atuais["MQ2"].data_leitura.strftime("%d/%m %H:%M")
        ]) if sensores_atuais["MQ2"] else "[]",
    }

    return render(request, "last-read.html", context)

def remover_sensor(request, id):
    sensor = TipoSensor.objects.get(id=id)
    sensor.delete()
    return redirect('painel_adm')

@login_required
def temperatura(request):
    # Busca todas as leituras em ordem cronológica
    sensores = LeituraSensor.objects.select_related("tipo_sensor").order_by("data_leitura")
    
    temperatura_data = [s.valor_percentual for s in sensores if s.tipo_sensor.nome == "TEMPERATURA"]
    umidade_data = [s.valor_percentual for s in sensores if s.tipo_sensor.nome == "UMIDADE"]
    timestamps = [s.data_leitura.strftime("%H:%M") for s in sensores if s.tipo_sensor.nome == "TEMPERATURA"]

    context = {
        "temperatura_data": temperatura_data,
        "umidade_data": umidade_data,
        "timestamps": timestamps,
    }
    return render(request, 'temperatura.html', context)

#crud usuário
def cadastrar_usuarios(request):
    if request.method == "POST":
        data = request.POST.copy()
        data["username"] = data.get("email") #email é utilizado como username
        form = FormularioCriacaoUsuario(data)
        if form.is_valid():
            user = form.save()
            messages.success(request, "Usuário cadastrado com sucesso!")
            return redirect("painel_adm")
        else:
            messages.error(request, "Erro ao cadastrar usuário. Verifique os campos.")
    else:
        form = FormularioCriacaoUsuario()

    return render(request, "user/admin/cadastrar_usuarios.html", {"form": form})

def remover_usuarios(request, id):
    usuario = User.objects.get(id=id)
    usuario.delete()
    return redirect('gerir_usuarios')

def mostrar_usuario(request, id):
    usuario = User.objects.get(id=id)
    return render(request, 'user/mostrar_usuario.html', {'usuario': usuario})

#tela administrativa
def painel_adm(request):
    search_query = request.GET.get('search', '')
    if search_query:
        users = User.objects.filter(
            Q(username__icontains=search_query) |
            Q(email__icontains=search_query)
        ).order_by('username')
    else:
        users = User.objects.all().order_by('username')

    sensores = TipoSensor.objects.all().order_by('nome')
    context = {
        'users': users,
        'search_query': search_query,
        'sensores': sensores,
    }
    return render(request, 'user/admin/painel_adm.html', context)