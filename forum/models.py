from django.db import models

# Create your models here.

import datetime 
from django.utils import timezone

class Pergunta(models.Model):
    titulo = models.CharField(max_length= 200, null = False)
    detalhe = models.TextField(null = False)
    tentativa = models.TextField()
    data_criacao = models.DateTimeField("Criado em: ")
    usuario = models.CharField(max_length=200, null = False, default="anônimo")

    def __str__(self):
        return "[" + str(self.id) + "]" + self.titulo
    
    def foi_publicado_recentemente(self):
        return self.data_criacao >= timezone.now() - datetime.timedelta(days=1)
    
    def string_detalhada(self):
        return "id: " + str(self.id) + "; titulo: " + str(self.titulo) + "; detalhe: " + str(self.detalhe) + "; tentativa: " + str(self.tentativa) + "; data de criação: " + str(self.data_criacao) + "; usuário: " + str(self.usuario)
    

class Resposta(models.Model):
    Pergunta = models.ForeignKey(Pergunta, on_delete=models.CASCADE)
    texto = models.TextField(null = False)
    votos = models.IntegerField(null=False)
    data_criacao = models.DateTimeField("Criado em: ")
    usuario = models.CharField(max_length=200, null = False, default="anônimo")

    def __str__(self):
        return "[" + str(self.id) + "]" + self.texto
    
    def foi_publicado_recentemente(self):
        return self.data_criacao >= timezone.now() - datetime.timedelta(days=1)
    

