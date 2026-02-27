from django.urls import path
from contact_site.views import views

app_name = "site"

urlpatterns = [
    path("ACJR/Home", views.index, name="index"),
    path("ACJR/Contato", views.form_email, name="contato"),
    path("ACJR/Obrigado", views.obrigado, name="obrigado"),
]