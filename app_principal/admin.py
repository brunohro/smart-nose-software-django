from django.contrib import admin
from .models import TipoSensor, LeituraSensor, Experimento

@admin.register(Experimento)
class ExperimentoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'descricao', 'data_inicio', 'data_fim', 'ativo')
    search_fields = ('nome',)

@admin.register(TipoSensor)
class TipoSensorAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome')
    search_fields = ('nome',)


@admin.register(LeituraSensor)
class LeituraSensorAdmin(admin.ModelAdmin):
    list_display = ('id', 'tipo_sensor', 'valor_percentual', 'data_leitura')
    list_filter = ('tipo_sensor', 'data_leitura')
    search_fields = ('tipo_sensor__nome',)
