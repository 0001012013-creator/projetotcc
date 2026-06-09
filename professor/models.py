from django.db import models
from accounts.models import User
from administrador.models import Turma


# ─────────────────────────────────────────────
# ATIVIDADE
# ─────────────────────────────────────────────
class Atividade(models.Model):

    turma = models.ForeignKey(
        Turma,
        on_delete=models.CASCADE,
        related_name='atividades'
    )

    titulo = models.CharField(
        max_length=200
    )

    descricao = models.TextField()

    data_criacao = models.DateTimeField(
        auto_now_add=True
    )

    data_entrega = models.DateField(
        null=True,
        blank=True
    )

    nota_maxima = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        default=10
    )

    def __str__(self):
        return self.titulo


# ─────────────────────────────────────────────
# CRITÉRIOS DE CORREÇÃO
# ─────────────────────────────────────────────
class CriterioAtividade(models.Model):

    atividade = models.ForeignKey(
        Atividade,
        on_delete=models.CASCADE,
        related_name='criterios'
    )

    palavra_chave = models.CharField(
        max_length=100
    )

    peso = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        default=1
    )

    def __str__(self):
        return f'{self.palavra_chave} ({self.peso})'


# ─────────────────────────────────────────────
# ENTREGA DO ALUNO
# ─────────────────────────────────────────────
class EntregaAtividade(models.Model):

    atividade = models.ForeignKey(
        Atividade,
        on_delete=models.CASCADE,
        related_name='entregas'
    )

    aluno = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        limit_choices_to={
            'user_type': 'aluno'
        }
    )

    resposta = models.TextField()

    nota = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        default=0
    )

    feedback = models.TextField(
        blank=True,
        null=True
    )

    corrigida = models.BooleanField(
        default=False
    )

    data_envio = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f'{self.aluno} - {self.atividade}'