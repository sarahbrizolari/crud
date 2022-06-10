from django.db import models


class Carro(models.Model):
    placa = models.CharField(max_length=100)
    nome = models.CharField(max_length=30)
    marca = models.CharField(max_length=100)
    modelo = models.CharField(max_length=100)
    anoFabricacao = models.CharField(max_length=30)
    anoModelo = models.CharField(max_length=100)
    cor = models.CharField(max_length=100)

    def _str_(self):
        return self.placa


class Cliente(models.Model):
    CPF = models.CharField(max_length=100)
    nome = models.CharField(max_length=30)
    telefone = models.CharField(max_length=100)
    endereco = models.CharField(max_length=100)
    cidade = models.CharField(max_length=30)
    nomePai = models.CharField(max_length=100)
    nomeMae = models.CharField(max_length=100)
    email = models.CharField(max_length=100)

    def _str_(self):
        return self.CPF


class Funcionario(models.Model):
    CPF = models.CharField(max_length=100)
    nome = models.CharField(max_length=30)
    salario = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    telefone = models.CharField(max_length=30)
    endereco = models.CharField(max_length=100)

    def _str_(self):
        return self.CPF


class Fornecedor(models.Model):
    CNPJ = models.CharField(max_length=100)
    nome = models.CharField(max_length=30)
    telefone = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    endereco = models.CharField(max_length=100)

    def _str_(self):
        return self.CNPJ


class Seguranca(models.Model):
    CPF = models.CharField(max_length=100)
    nome = models.CharField(max_length=30)
    email = models.CharField(max_length=100)
    telefone = models.CharField(max_length=30)

    def _str_(self):
        return self.CPF


class Vagas(models.Model):
    descricao = models.CharField(max_length=30)

    def _str_(self):
        return self.descricao


class Locacao(models.Model):
    cliente = models.CharField(max_length=100)
    carro = models.CharField(max_length=30)
    funcionario = models.CharField(max_length=100)
    dataLocacao = models.CharField(max_length=30)
    valor = models.CharField(max_length=100)
    dataDevolucao = models.CharField(max_length=30)

    def _str_(self):
        return self.cliente

