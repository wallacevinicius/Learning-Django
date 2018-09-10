from django.shortcuts import render
from django.http import HttpResponse

def clientes(request, id):
    return HttpResponse(id)

def clienteNome(request, nome):
    return HttpResponse("<h1 style='font-family:Roboto;'>Ola <span style='text-transform:uppercase;'>%s</span></h1>" % nome)
