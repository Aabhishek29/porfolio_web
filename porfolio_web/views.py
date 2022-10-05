from django.shortcuts import render
from porfolio_web.settings import STATIC_URL


# Create your views here.
def home(request):
    return render(request, 'home.html', {'STATIC_URL': STATIC_URL})


def contactme(request):
    return render(request, 'contactme.html', {'STATIC_URL': STATIC_URL})


def projects(request):
    return render(request, 'projects.html', {'STATIC_URL': STATIC_URL})
