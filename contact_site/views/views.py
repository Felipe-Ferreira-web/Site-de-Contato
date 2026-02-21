from django.shortcuts import render


def index(request):
    
    context = {
        "site_title": "Home"
    }
    return render(
        request,
        "index.html", context
    )

def contato(request):
    
    context = {
        "site_title": "Formulário de Contato"
    }
    return render(
        request,
        "contato.html", context
    )   