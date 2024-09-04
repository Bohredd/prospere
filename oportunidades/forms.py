from django import forms

class InteresseForm(forms.Form):
    def __init__(self, *args, **kwargs):
        requisito = kwargs.pop('requisito', None)
        super(InteresseForm, self).__init__(*args, **kwargs)

        if requisito:
            if requisito.precisa_texto:
                self.fields['texto'] = forms.CharField(
                    label=requisito.helptext_texto if requisito.helptext_texto else '',
                    required=True,
                )
            if requisito.precisa_arquivos:
                self.fields['arquivos'] = forms.FileField(
                    label=requisito.helptext_arquivos if requisito.helptext_arquivos else '',
                    required=True,
                    widget=forms.FileInput(attrs={'multiple': False}),
                )
            if requisito.precisa_foto:
                self.fields['foto'] = forms.ImageField(
                    label=requisito.helptext_foto if requisito.helptext_foto else '',
                    required=True,
                )
            if requisito.precisa_links:
                self.fields['links'] = forms.URLField(
                    label=requisito.helptext_links if requisito.helptext_links else '',
                    required=True,
                )
            if requisito.precisa_checkbox:
                self.fields['checkbox'] = forms.BooleanField(
                    label=requisito.helptext_checkbox if requisito.helptext_checkbox else '',
                    required=True,
                )

    def clean_arquivos(self):
        files = self.files.getlist('arquivos')
        if not files and 'arquivos' in self.fields and self.fields['arquivos'].required:
            raise forms.ValidationError('Este campo é obrigatório.')
        return files
