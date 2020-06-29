from django import forms


class NewsletterForm(forms.Form):
    name = forms.CharField(
        widget=forms.TextInput(
            attrs={
            'class':'form-control form-control-lg',
            'placeholder':'Informar Nome'
            }),
        label='Nome', max_length=100)
    email = forms.EmailField(
        widget=forms.TextInput(
            attrs={
                'class':'form-control form-control-lg',
                'placeholder':'Informar Email'
                }),
            label='E-mail')
