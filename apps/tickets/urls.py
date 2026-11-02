from django.urls import path
from . import views

urlpatterns = [
    path("novo/", views.novo_chamado, name="novo_chamado"),
    path("<uuid:ticket_id>/", views.detalhe_chamado, name="detalhe_chamado"),
    path("", views.chamados, name="chamados"),
]
