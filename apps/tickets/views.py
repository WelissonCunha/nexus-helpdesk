
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.shortcuts import redirect
from apps.organizations.models import Organization

from .models import Ticket


@login_required
def chamados(request):
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

    pesquisa = request.GET.get("q", "").strip()

    if pesquisa:
        chamados = chamados.filter(
            Q(title__icontains=pesquisa) |
            Q(description__icontains=pesquisa)
        )

    status = request.GET.get("status", "")
    status_validos = [
        choice[0] for choice in Ticket.Status.choices
    ]

    if status in status_validos:
        chamados = chamados.filter(status=status)

    prioridade = request.GET.get("priority", "")
    prioridades_validas = [
        choice[0] for choice in Ticket.Priority.choices
    ]

    if prioridade in prioridades_validas:
        chamados = chamados.filter(priority=prioridade)

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


@login_required
def detalhe_chamado(request, ticket_id):
    organizacoes_do_usuario = request.user.memberships.values_list(
        "organization_id",
        flat=True
    )

    chamado = get_object_or_404(
        Ticket.objects.select_related(
            "organization",
            "requester",
            "assigned_to"
        ).prefetch_related("comments__author"),
        id=ticket_id,
        organization_id__in=organizacoes_do_usuario
    )

    context = {
        "chamado": chamado,
    }

    return render(request, "chamados/detalhe.html", context)


@login_required
def novo_chamado(request):
    # Busca somente as organizações às quais o usuário pertence.
    organizacoes = Organization.objects.filter(
        memberships__user=request.user
    ).distinct().order_by("name")

    if request.method == "POST":
        titulo = request.POST.get("title", "").strip()
        descricao = request.POST.get("description", "").strip()
        prioridade = request.POST.get("priority", "")
        organizacao_id = request.POST.get("organization", "")

        # Validação dos campos obrigatórios.
        if not titulo or not descricao or not organizacao_id:
            messages.error(
                request,
                "Preencha todos os campos obrigatórios."
            )
            return render(
                request,
                "chamados/novo_chamado.html",
                {"organizacoes": organizacoes}
            )

        # Valida se a organização realmente pertence ao usuário.
        organizacao = get_object_or_404(
            organizacoes,
            id=organizacao_id
        )

        # Valida a prioridade recebida.
        prioridades_validas = [
            choice[0] for choice in Ticket.Priority.choices
        ]

        if prioridade not in prioridades_validas:
            messages.error(request, "Selecione uma prioridade válida.")
            return render(
                request,
                "chamados/novo_chamado.html",
                {"organizacoes": organizacoes}
            )

        # Cria o chamado.
        chamado = Ticket.objects.create(
            organization=organizacao,
            title=titulo,
            description=descricao,
            requester=request.user,
            priority=prioridade,
            status=Ticket.Status.OPEN
        )

        messages.success(request, "Chamado criado com sucesso!")

        return redirect("detalhe_chamado", ticket_id=chamado.id)

    return render(
        request,
        "chamados/novo_chamado.html",
        {
            "organizacoes": organizacoes,
            "priority_choices": Ticket.Priority.choices,
        }
    )
