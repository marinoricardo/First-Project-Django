from tabnanny import verbose
from tkinter import CASCADE
from django.db import models
from django.utils import timezone


# Create your models here.

# class Person(models.Model):
#     first_name = models.CharField(max_length=30)
#     las_name = models.CharField
class Categoria(models.Model):
    nome = models.CharField(max_length=100)
    dt_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome

class Transacao(models.Model):
    data = models.DateTimeField(default=timezone.now)
    descricao = models.CharField(max_length=250)
    valor = models.DecimalField(max_digits=7,decimal_places=2)
    categoria = models.ForeignKey(Categoria,on_delete=models.CASCADE)
    observacoes = models.TextField(null=True,blank=True)

    class Meta:
        verbose_name_plural = 'Transacoes'
    def __str__(self):
        return self.descricao
