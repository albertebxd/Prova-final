from django import forms
from .models import Pessoas

class PessoasForm(forms.ModelForm):
    
    class Meta:
        model = Pessoas
        fields = ('nome','idade','departamento','telefone',)
