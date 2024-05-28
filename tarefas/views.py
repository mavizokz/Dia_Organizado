from django.shortcuts import render
from .models import Tarefas

def tarefas_pendentes_list(request):
    tarefas_pendentes = Tarefas.objects.filter(status='pendente')
    return render(request, 'tarefas/tarefas_pendentes.html',
                  {'tarefas_pendnetes': tarefas_pendentes})
