from django import forms

class ContactForm(forms.Form):
    name = forms.CharField( 
        error_messages={'required': 'Por favor, preencha o nome.'}, label="Nome"
    )
    email = forms.EmailField( 
        error_messages={'required': 'O E-mail é obrigatório.', 'invalid': 'Formato de E-mail inválido.'}, label="E-mail"
    )
    object = forms.CharField(
 
        error_messages={'required': 'Coloque um assunto.'},label="Assunto"
    )
    message = forms.CharField( 
        error_messages={'required': 'Escreva uma mensagem.'}, label="Mensagem"
    )