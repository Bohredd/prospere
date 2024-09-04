from django import forms
from core.models import RespostaInteresse

class RespostaInteresseForm(forms.ModelForm):
    resposta_requisito_pk = forms.IntegerField(widget=forms.HiddenInput(), required=False)

    class Meta:
        model = RespostaInteresse
        fields = ['texto', 'aprovado']
        widgets = {
            'texto': forms.Textarea(attrs={'rows': 4, 'cols': 40}),
        }
