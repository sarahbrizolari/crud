from django.shortcuts import render, redirect

from estacionamento.forms import LocacaoForm
from estacionamento.models import Locacao

def list_Locacao(request):
    Locacoes = Locacao.objects.all()
    return render(request, 'Locacao.html', {'Locacoes': Locacoes})


def create_Locacao(request):
    form = LocacaoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('list_Locacao')
    return render(request, 'Locacao-form.html', {'form': form})


def update_Locacao(request, id):
    Loc = Locacao.objects.get(id=id)
    form = LocacaoForm(request.POST or None, instance=Loc)
    if form.is_valid():
        form.save()
        return redirect('list_Locacao')
    return render(request, 'Locacao-form.html', {'form': form, 'Locacao': Locacao})


def delete_Locacao(request, id):
    Loc = Locacao.objects.get(id=id)
    if request.method == 'POST':
        Loc.delete()
        return redirect('list_Locacao')
    return render(request, 'Locacao-delete-confirm.html', {'Loc': Loc})