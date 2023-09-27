from django.shortcuts import render
from visitantes.forms import VisitorForm


def visitor_registration(request):
    
    form = VisitorForm()

    context = {
        "nome_pagina": "Registrar visitante",
        "form": form
    }

    return render(request, 'visitor_registration.html', context)
