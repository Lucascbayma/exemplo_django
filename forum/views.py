from django.shortcuts import render
from django.http import HttpResponse, Http404

from .models import Pergunta, Resposta
from django.views import View

from django.utils import timezone
from django.shortcuts import redirect
from django.urls import reverse

class MainView(View):
    def get(self, request):
        lista_ultimas_questões = Pergunta.objects.order_by("-data_criacao")
        contexto = {'perguntas': lista_ultimas_questões}
        return render(request,'forum/index.html', contexto)
    
class PerguntaView(View):
    def get(self, request, pergunta_id):
        try:
            pergunta = Pergunta = Pergunta.objects.get(pk=pergunta_id)
        except Pergunta.DoesNotExist:
            raise Http404("pergunta inexistente")
        contexto = {'pergunta': pergunta}
        return render(request, 'forum/detalhe.html', contexto)