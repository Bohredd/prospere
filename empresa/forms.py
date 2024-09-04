from django import forms
from core.models import RespostaInteresse

class RespostaInteresseForm(forms.ModelForm):
    class Meta:
        model = RespostaInteresse
        fields = ['texto', 'aprovado']
        widgets = {
            'texto': forms.Textarea(attrs={'rows': 4, 'cols': 40}),
        }
