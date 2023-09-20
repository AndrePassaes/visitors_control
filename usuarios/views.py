from django.shortcuts import render
from visitantes.models import Visitor


def index(request):

    all_visitors = Visitor.objects.all()

    context = {
        "nome_pagina": "Início do Dashboard",
        "all_visitors": all_visitors,
    }
    return render(request, 'index.html', context)
