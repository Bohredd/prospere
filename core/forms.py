from django import forms
from .models import Solicitacao

class RequisitoOportunidadeForm(forms.ModelForm):
    class Meta:
        model = Solicitacao
        fields = [
            'curriculo',
            'descricao',
            'email_contato',
            'telefone_contato',
            'endereco',
        ]
        widgets = {
            'curriculo': forms.FileInput(attrs={'class': 'form-control'}),
            'descricao': forms.Textarea(attrs={'class': 'form-control'}),
            'email_contato': forms.EmailInput(attrs={'class': 'form-control'}),
            'telefone_contato': forms.TextInput(attrs={'class': 'form-control'}),
            'endereco': forms.Textarea(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        tipo_solicitacao = kwargs.pop('tipo_solicitacao', None)
        requisito = kwargs.pop('requisito', None)
        super().__init__(*args, **kwargs)

        if requisito:
            if not requisito.precisa_curriculo:
                self.fields.pop('curriculo')
            else:
                self.fields['curriculo'].required = True

            if not requisito.precisa_descricao:
                self.fields.pop('descricao')
            else:
                self.fields['descricao'].required = True

            if not requisito.precisa_email_contato:
                self.fields.pop('email_contato')
            else:
                self.fields['email_contato'].required = True

            if not requisito.precisa_telefone_contato:
                self.fields.pop('telefone_contato')
            else:
                self.fields['telefone_contato'].required = True

            if not requisito.precisa_endereco:
                self.fields.pop('endereco')
            else:
                self.fields['endereco'].required = True
