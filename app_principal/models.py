from django.db import models
from django.utils import timezone

class Experimento(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField(blank=True, null=True)
    data_inicio = models.DateTimeField(auto_now_add=True)
    data_fim = models.DateTimeField(blank=True, null=True)
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return self.nome
    
class TipoSensor(models.Model):
    nome = models.CharField(max_length=50, unique=True)
    funcao = models.TextField(blank=True, null=True)
    data_criacao = models.DateTimeField(auto_now_add=True)
    exibir = models.BooleanField(default=True)

    def __str__(self):
        return self.nome
    
class LeituraSensor(models.Model):
    tipo_sensor = models.ForeignKey(TipoSensor, on_delete=models.CASCADE, related_name="leituras")
    valor_percentual = models.FloatField(help_text="Valor em porcentagem ( 0 a 100 )")
    data_leitura = models.DateTimeField(auto_now_add=True)
    experimento = models.ForeignKey(Experimento, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.tipo_sensor.nome} - {self.valor_percentual} ({self.data_leitura.strftime('%d/%m/%Y %H:%M')})"
