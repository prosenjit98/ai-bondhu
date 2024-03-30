from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from clients.models import Client

# Create your views here.

def clients_index(request):
    clients = Client.objects.all()
    template = loader.get_template('clients/index.html')
    context = {
        "clients": clients
    }
    return HttpResponse(template.render(context, request))

def clients_show(request, id):
    client = Client.objects.get(id=id)
    template = loader.get_template('show.html')
    context = {
        "client": client
    }
    return HttpResponse(template.render(context, request))
