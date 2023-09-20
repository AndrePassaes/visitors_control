from django.shortcuts import render


def visitor_registration(request):
    context = {}

    return render(request, 'visitor_registration.html', context)
