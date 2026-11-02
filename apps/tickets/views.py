from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import render

from .models import Ticket


@login_required
def chamados(request):
    # Primeiro: restringir aos chamados das organizações
    # das quais o usuário é membro.
    organizacoes_do_usuario = request.user.memberships.values_list(
        "organization_id",
        flat=True
    )

    chamados = (
        Ticket.objects
        .filter(organization_id__in=organizacoes_do_usuario)
        .select_related(
            "organization",
            "requester",
            "assigned_to"
        )
        .order_by("-created_at")
    )

    # Pesquisa por título ou descrição.
    pesquisa = request.GET.get("q", "").strip()

    if pesquisa:
        chamados = chamados.filter(
        Q(title__icontains=pesquisa) |
        Q(description__icontains=pesquisa)
    )

    # Filtro de status.
    status = request.GET.get("status", "")

    status_validos = [
        choice[0] for choice in Ticket.Status.choices
    ]

    if status in status_validos:
        chamados = chamados.filter(status=status)

    # Filtro de prioridade.
    prioridade = request.GET.get("priority", "")

    prioridades_validas = [
        choice[0] for choice in Ticket.Priority.choices
    ]

    if prioridade in prioridades_validas:
        chamados = chamados.filter(priority=prioridade)

    # Paginação: 10 chamados por página.
    paginator = Paginator(chamados, 10)
    pagina = paginator.get_page(request.GET.get("page"))

    context = {
        "pagina": pagina,
        "pesquisa": pesquisa,
        "status_selecionado": status,
        "prioridade_selecionada": prioridade,
        "status_choices": Ticket.Status.choices,
        "priority_choices": Ticket.Priority.choices,
        "possui_organizacao": request.user.memberships.exists(),
    }

    return render(request, "chamados/chamado.html", context)
