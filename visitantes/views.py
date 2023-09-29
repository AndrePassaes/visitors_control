from django.contrib import messages
from django.shortcuts import render, redirect
from visitantes.forms import VisitorForm



def visitor_registration(request):    
    form = VisitorForm()
    if request.method == "POST":
        form = VisitorForm(request.POST)        
        if form.is_valid():
            visitor = form.save(commit=False)
            visitor.registered_by = request.user.concierge
            visitor.save()
            messages.success(
                request, "Visitante registrado com sucesso!"
                )
            return redirect("index")
    context = {
        "nome_pagina": "Registrar visitante",
        "form": form
    }

    return render(request, 'visitor_registration.html', context)
