from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    response = "<a href='/repositorio'>Ir al administrador</a>"
    return HttpResponse(response)