from django.contrib import admin
from django.urls import path, include
from app_principal.views import (
    index, dashboard, login_view, logout_view, user_detail, sensores, temperatura,
    mostrar_usuario, cadastrar_usuarios, remover_usuarios, ultima_leitura,
    painel_adm, cadastrar_sensor, remover_sensor, iniciar_experimento, encerrar_experimento, exportar_experimento_csv, listar_experimento, remover_experimento
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('dashboard/', dashboard, name='dashboard'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('user/<int:pk>/', user_detail, name='user_detail'),
    path('sensores/', sensores, name='sensores'),
    path('temperatura/', temperatura, name='temperatura'),
    path('ultima_leitura/', ultima_leitura, name='ultima_leitura'),
    path('iniciar_experimento/', iniciar_experimento, name='iniciar_experimento'),
    path('encerrar_experimento/<int:id>', encerrar_experimento, name='encerrar_experimento'),
    path('exportar_experimento_csv/<int:id>', exportar_experimento_csv, name='exportar_experimento_csv'),
    path('listar_experimento/', listar_experimento, name='listar_experimento'),
    path('remover_experimento/<int:id>', remover_experimento, name='remover_experimento'),
    

    # Rotas do administrador
    path('mostrar_usuario/<int:id>', mostrar_usuario, name='mostrar_usuario'),
    path('cadastrar_usuarios/', cadastrar_usuarios, name='cadastrar_usuarios'),
    path('remover_usuarios/<int:id>', remover_usuarios, name='remover_usuarios'),
    path('cadastrar_sensor/', cadastrar_sensor, name='cadastrar_sensor'),
    path('remover_sensor/<int:id>', remover_sensor, name='remover_sensor'),
    path('painel_adm/', painel_adm, name='painel_adm'),

    # Rotas da API REST
    path('api/', include('app_principal.urls_api')),
]
