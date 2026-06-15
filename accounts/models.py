from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):

    USER_TYPE_CHOICES = (
        ('admin', 'Administrador'),
        ('professor', 'Professor'),
        ('aluno', 'Aluno'),
    )

    # tipo de usuário
    user_type = models.CharField(
        max_length=20,
        choices=USER_TYPE_CHOICES
    )

    # dados pessoais
    cpf = models.CharField(
        max_length=14,
        unique=True,
        null=True,
        blank=True
    )

    telefone = models.CharField(
        max_length=20,
        null=True,
        blank=True
    )

    endereco = models.TextField(
        null=True,
        blank=True
    )

    data_nascimento = models.DateField(
        null=True,
        blank=True
    )

    # foto
    foto = models.ImageField(
        upload_to='usuarios/',
        null=True,
        blank=True
    )

    # responsável (apenas aluno)
    nome_responsavel = models.CharField(
        max_length=255,
        null=True,
        blank=True
    )

    telefone_responsavel = models.CharField(
        max_length=20,
        null=True,
        blank=True
    )

    # email institucional (gerado pelo sistema)
    email = models.EmailField(
        unique=True
    )

    # email pessoal
    email_pessoal = models.EmailField(
        null=True,
        blank=True
    )

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return self.username


class SolicitacaoRecuperacao(models.Model):

    STATUS_CHOICES = (
        ('pendente', 'Pendente'),
        ('aprovado', 'Aprovado'),
        ('rejeitado', 'Rejeitado'),
    )

    email = models.EmailField()

    data_solicitacao = models.DateTimeField(
        auto_now_add=True
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='pendente'
    )

    def __str__(self):
        return self.email