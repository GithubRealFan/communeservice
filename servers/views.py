from django.http import HttpResponse
from django.shortcuts import render
from .models import Server

def index(request):
    servers = Server.objects.all()
    return render(request, 'index.html', {'servers' : servers})

def new(request):
    return HttpResponse('New Servers')
