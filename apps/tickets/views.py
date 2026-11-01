from django.contrib.auth.decorators import login_required
from django.shortcuts import render

@login_required
def chamados(request):
    return render(request, "chamados/chamado.html")
