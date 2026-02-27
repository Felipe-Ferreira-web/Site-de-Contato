from django.shortcuts import render, redirect
from contact_site.form import ContactForm
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.conf import settings


def index(request):
    
    context = {
        "site_title": "Home"
    }
    return render(
        request,
        "index.html", context
    )


def form_email(request):
    if request.method == "POST":

        form = ContactForm(request.POST)
        if form.is_valid():

            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            object = form.cleaned_data['object']
            message = form.cleaned_data['message']

            html_content = render_to_string('emails/email.html', {'name': name, 'email': email, 'object': object, 'message': message})

            text_content = strip_tags(html_content)

            email = EmailMultiAlternatives(object, text_content, settings.EMAIL_HOST_USER, [settings.EMAIL_HOST_USER])
            
            email.attach_alternative(html_content, 'text/html')

            email.send()
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