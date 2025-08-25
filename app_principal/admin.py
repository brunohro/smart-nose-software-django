from django.contrib import admin
from .models import TipoSensor, LeituraSensor

@admin.register(TipoSensor)
class TipoSensorAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome')
    search_fields = ('nome',)


@admin.register(LeituraSensor)
class LeituraSensorAdmin(admin.ModelAdmin):
    list_display = ('id', 'tipo_sensor', 'valor_percentual', 'data_criacao')
    list_filter = ('tipo_sensor', 'data_criacao')
    search_fields = ('tipo_sensor__nome',)
