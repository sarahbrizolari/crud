from django import forms
from estacionamento.models import Locacao, Carro, Cliente, Funcionario, Fornecedor, Seguranca, Vagas


class CarroForm(forms.ModelForm):
    class Meta:
        model = Carro
        fields = ['placa', 'nome', 'marca', 'modelo', 'anoFabricacao', 'anoModelo', 'cor']


class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['CPF', 'nome', 'telefone', 'endereco', 'cidade', 'nomePai', 'nomeMae', 'email']


class FuncionarioForm(forms.ModelForm):
    class Meta:
        model = Funcionario
        fields = ['CPF', 'nome', 'salario', 'email', 'telefone', 'endereco']


class FornecedorForm(forms.ModelForm):
    class Meta:
        model = Fornecedor
        fields = ['CNPJ', 'nome', 'telefone', 'email', 'endereco']


class SegurancaForm(forms.ModelForm):
    class Meta:
        model = Seguranca
        fields = ['CPF', 'nome', 'email', 'telefone']


class VagasForm(forms.ModelForm):
    class Meta:
        model = Vagas
        fields = ['descricao']


class LocacaoForm(forms.ModelForm):
    class Meta:
        model = Locacao
        fields = ['cliente', 'carro', 'funcionario', 'dataLocacao', 'valor', 'dataDevolucao']