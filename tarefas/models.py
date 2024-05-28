from django.db import models

class Tarefas(models.Model):
    OPCOES_STATUS = (
        ('concluido', 'Conluido'),
        ('pendente', 'Pendente'),
        ('adiado', 'Adiado'),
    )

    OPCOES_CATEGORIA = (
        ('urgnete', 'Urgente'),
        ('importante', 'Importante'),
        ('precisa ser feito', 'Precisa ser feito'),
    )
    
    descricao = models.CharField(max_length=400)
    criacao = models.DateField(auto_now_add=True)
    categoria = models.CharField(max_length=25, choices=OPCOES_CATEGORIA, default='importante')
    status = models.CharField(max_length=25, choices=OPCOES_STATUS, default='pendente')