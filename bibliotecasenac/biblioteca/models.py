from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator
from django.core.exceptions import ValidationError
from django.utils import timezone
from datetime import timedelta
import os
# Create your models here.


class Usuario(AbstractUser):
    TIPO_USUARIO = (
        ('aluno', 'Aluno'),
        ('admin', 'Administrador'),
    )

    tipo_usuario = models.CharField(
        max_length=10,
        choices=TIPO_USUARIO,
        default='aluno',
        verbose_name='Tipo de Usuário'
    )

    email = models.EmailField(
        unique=True,
        verbose_name='E-mail',
    )

    data_cadastro = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Data de Cadastro'
    )
    
    class Meta:
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'
    
    
    def __str__(self):
        return f"{self.username} ({self.get_tipo_usuario_display()})"


    def is_admin(self):
        return self.tipo_usuario == 'admin'


    def pode_reservar(self):
        reservas_ativas = self.reservas.filter(status='ativa').count()
        return reservas_ativas < 3
    
class Autor(models.Model):
    nome = models.CharField(max_length=100, verbose_name='Nome do Autor')
    data_cadastro = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Data de Cadastro'
    )   
    
    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'Autor'
        verbose_name_plural = 'Autores'
        ording = ['nome']


class Livro(models.Model):
    TIPO_GENERO = [
        ('ficcao', 'Ficção'),
        ('nao_ficcao', 'Não Ficção'),
        ('fantasia', 'Fantasia'),
        ('aventura', 'Aventura'),
        ('romance', 'Romance'),
        ('suspense', 'Suspense'),
        ('terror', 'Terror'),
        ('biografia', 'Biografia'),
        ('autoajuda', 'Autoajuda'),
        ('educacional', 'Educacional'),
    ]
    
    titulo = models.CharField(max_length=200, verbose_name='Título do Livro')
    autor = models.ForeignKey(
        Autor,
        on_delete=models.CASCADE,
        related_name='livros',
        verbose_name='Autor',
        unique=True
    )
    
    genero =  models.CharField(
        max_length=20,
        choices=TIPO_GENERO,
        verbose_name='Gênero'
    )
    
    quantidade = models.PositiveIntegerField(
        default=1,
        validators=[MinValueValidator(0)],
        verbose_name='Quantidade Total'
    )
    
    quantidade_disponivel = models.PositiveIntegerField(
        default=1,
        validators=[MinValueValidator(0)],
        verbose_name='Quantidade Disponível'
    )
    
    data_cadastro = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Data de Cadastro'
    )
    
    class Meta:
        verbose_name = 'Livro'
        verbose_name_plural = 'Livros'
        ordering = ['titulo']
    
    def __str__(self):
        return self.titulo
    
    def save(self, *args, **kwargs):
        
        if not self.pk:
            self.quantidade_disponivel = self.quantidade
        
        if self.quantidade_disponivel > self.quantidade:
            self.quantidade_disponivel = self.quantidade
        
        super().save(*args, **kwargs)
        