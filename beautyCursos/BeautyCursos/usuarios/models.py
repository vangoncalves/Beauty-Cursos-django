from django.db import models

# Create your models here.
class Usuarios(models.Model):
    idUsuario = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=300, null=False)
    cpf = models.CharField(max_length=11, null=False)
    telefone = models.CharField(max_length=15, null=False)
    email = models.CharField(max_length=300, null=True)