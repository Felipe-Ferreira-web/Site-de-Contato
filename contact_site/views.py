from django.shortcuts import render, redirect
from contact_site.form import ContactForm
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.conf import settings


def Home(request):
    """
    View to display the Home page.

    Sets the page's sub-title to "Home" and renders the main landing 
    page containing the 'About' and 'Services' sections.

    Args:
        request: The HTTP request object.

    Returns:
        HttpResponse: Rendered 'Home.html' with the site_title context.
    """  
    context = {
        "site_title": "Home"
    }
    return render(
        request,
        "Home.html", context
    )


def form_email(request):
    """
    View to process the contact form, validate data, and dispatch emails.

    Uses EmailMultiAlternatives to send a hybrid email (HTML and plain text)
    based on a pre-defined template.

    Parameters:
    -----------
    request: HttpRequest
        request (HttpRequest): The HTTP request object containing form data.
    Return:
    --------
    HttpResponse:
    - Redirection to 'site:obrigado' upon successful validation and dispatch.
    - Rendered 'contato.html' with the form context for GET or invalid POST.
    - Rendered 'error.html' if an Exception occurs and raises the context with the status
    """
    if request.method == "POST":

        form = ContactForm(request.POST)
        if form.is_valid():

            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']

            html_content = render_to_string('emails/email.html', {'name': name, 'email': email, 'subject': subject, 'message': message})

            text_content = strip_tags(html_content)

            email = EmailMultiAlternatives(subject, text_content, settings.EMAIL_HOST_USER, [settings.EMAIL_HOST_USER])
            
            email.attach_alternative(html_content, 'text/html')

            try:
                email.send()
                return redirect("site:obrigado")
            except Exception as e:
                print(f"Erro ao enviar e-mail: {e}")

                context = {
                    'form': form,
                    'site_title': "Contato",
                }
            return render(request, 'errors/error.html', context, status=500)
            
            
    else:
        form = ContactForm()

    context = {"form": form, 'site_title': 'Contato'}

    return render(request, "contato.html", context ) 


def obrigado(request):
    """
    View to display the Obrigado page.

    Sets the page's sub-title to "Obrigado pelo Contato" and renders the feedback page. 

    Args:
        request: The HTTP request object.

    Returns:
        HttpResponse: Rendered 'obrigado.html' with the site_title context.
    """

    context = {
        "site_title": "Obrigado pelo Contato"
    }
    return render(
        request,
        "obrigado.html", context
    )

def error_page(request):
    """
    View to display the Error page.

    Sets the page's sub-title to "Error" and renders the feedback page. 

    Args:
        request: The HTTP request object.

    Returns:
        HttpResponse: Rendered 'error.html' with the site_title context.
    """

    context = {
        "site_title": "Error"
    }
    return render(
        request,
        "errors/error.html", context
    )