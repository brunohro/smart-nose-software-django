from django.db import models
from django.utils import timezone

class TipoSensor(models.Model):
    nome = models.CharField(max_length=50, unique=True)
    descricao = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nome
    

class LeituraSensor(models.Model):
    tipo_sensor = models.ForeignKey(TipoSensor, on_delete=models.CASCADE, related_name="leituras")
    valor_percentual = models.FloatField(help_text="Valor em porcentagem ( 0 a 100 )")
    data_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.tipo_sensor.nome} - {self.valor_percentual} ({self.data_criacao.strftime('%d/%m/%Y %H:%M')})"
    
    @classmethod
    def dias_disponiveis(cls):
        """Retorna os dias que possuem leituras registradas."""
        return (
            cls.objects
            .dates('data_criacao', 'day', order='DESC')
        )
    
    @classmethod
    def leituras_por_dia(cls, dia_selecionado, tipo_sensor=None):
        """Retorna leituras filtradas por dia e, opcionalmente, por tipo de sensor."""
        consultas = cls.objects.filter(data_criacao__date=dia_selecionado)
        if tipo_sensor:
            consultas = consultas.filter(tipo_sensor=tipo_sensor)
        return consultas.order_by('data_criacao')
