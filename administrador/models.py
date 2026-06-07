from django.db import models
from accounts.models import User


class Turma(models.Model):

    nome = models.CharField(
        max_length=100
    )

    descricao = models.TextField(
        blank=True,
        null=True
    )

    professor = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        limit_choices_to={
            'user_type': 'professor'
        },
        related_name='turmas_professor'
    )

    alunos = models.ManyToManyField(
        User,
        blank=True,
        related_name='turmas_aluno',
        limit_choices_to={
            'user_type': 'aluno'
        }
    )

    data_criacao = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.nome