from django.shortcuts import redirect, render

from Pessoas.forms import PessoasForm
from .models import Pessoas
# Create your views here.

def list_Pessoas(request):
    Pessoas = Pessoas.objects.all()
    return render(request, "Pessoas.html", {'Pessoas': Pessoas})

def criar_Pessoas(request):
    form = PessoasForm
    form.save()
    return render(request, 'list_Pessoas', {'form': form})




def editar_Pessoas(request,id):
    Pessoa = Pessoa.objects.get(id=id)
    form = PessoasForm(request.POST, instance=Pessoa)
    return redirect ('list_Pessoas'), {'form': form, 'Pessoas' : Pessoas}

def excluir_Pessoas(request,id) :
    Pessoas = Pessoas.objects.get (id=id)
    
    if request.method == 'POST':
        Pessoas.delete()
        return redirect (list_Pessoas)
    return render(request, 'excluir_pessoas.html', {'Pessoas': Pessoas})  