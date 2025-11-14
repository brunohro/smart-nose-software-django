from rest_framework import serializers
from .models import TipoSensor, LeituraSensor

class TipoSensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoSensor
        fields = '__all__'


class LeituraSensorSerializer(serializers.ModelSerializer):
    tipo_sensor_nome = serializers.CharField(source='tipo_sensor.nome', read_only=True)

    class Meta:
        model = LeituraSensor
        fields = ['id', 'tipo_sensor', 'tipo_sensor_nome', 'valor_percentual', 'data_criacao']
