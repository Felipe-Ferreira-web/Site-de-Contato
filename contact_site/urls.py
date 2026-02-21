from django.urls import path
from contact_site.views import views

app_name = "site"

urlpatterns = [
    path("ACJR/Home", views.index, name="index"),
    path("ACJR/Contato", views.contato, name="contato"),
]