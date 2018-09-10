from django.db import models

# Create your models here.

class CPF(models.Model):
    numero = models.CharField(max_length=15)
    data_exp = models.DateTimeField(auto_now=False)

    def __str__(self):
        return self.numero

class Cliente(models.Model):
    nome = models.CharField(max_length=255, blank=False, null=False)
    address = models.CharField(max_length=255, blank=False, null=False)
    idade = models.IntegerField()
    email = models.EmailField()
    cpf = models.OneToOneField(CPF, on_delete=models.DO_NOTHING, null=True, blank=True)

    def __str__(self):
        return self.nome

class Telefone(models.Model):
    numero = models.CharField(max_length=20)
    descricao = models.CharField(max_length=100)
    cliente = models.ForeignKey(Cliente, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.descricao + ' - ' + self.numero

class Produtos(models.Model):
    nome = models.CharField(max_length=255, blank=False, null=False)
    preco = models.IntegerField()
    quantidade = models.IntegerField()
    descricao = models.CharField(max_length=255, blank=False, null=False)

