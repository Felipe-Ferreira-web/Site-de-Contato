from django.shortcuts import render, redirect
from contact_site.form import ContactForm
from django.core.mail import send_mail
from decouple import config


def index(request):
    
    context = {
        "site_title": "Home"
    }
    return render(
        request,
        "index.html", context
    )


def contato(request):
    if request.method == "POST":

        form = ContactForm(request.POST)
        if form.is_valid():

            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            object = form.cleaned_data['object']
            message = form.cleaned_data['message']

            send_mail(
                subject=object,
                message=(f"Olá, eu sou {name}\n\n{message}.\n\nAtenciosamente {name}\n\n*Lembrete: Este é um endereço de email automático, para responder este email, envie-o para: {email}"), 
                from_email=email, 
                recipient_list=[config("EMAIL_HOST_USER")],
                fail_silently=False),
            return redirect("site:obrigado")
            
    else:
        form = ContactForm()

    context = {"form": form, 'site_title': 'Contato'}

    return render(request, "contato.html", context ) 


def obrigado(request):

    context = {
        "site_title": "Obrigado pelo Contato"
    }
    return render(
        request,
        "obrigado.html", context
    )