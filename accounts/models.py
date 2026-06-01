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
    cpf = models.CharField(max_length=14, unique=True, null=True, blank=True)
    telefone = models.CharField(max_length=20, null=True, blank=True)
    endereco = models.TextField(null=True, blank=True)
    data_nascimento = models.DateField(null=True, blank=True)

    # foto
    foto = models.ImageField(
        upload_to='usuarios/',
        null=True,
        blank=True
    )

    # responsável (APENAS PARA ALUNO)
    nome_responsavel = models.CharField(max_length=255, null=True, blank=True)
    telefone_responsavel = models.CharField(max_length=20, null=True, blank=True)

    # email será usado como login
    email = models.EmailField(unique=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']