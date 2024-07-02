from django.shortcuts import render
from .models import ItemDB

# Create your views here.

def Inicio(request):   
    return render(request, 'inicio.html',)

def vitrina(request):
     items = ItemDB.objects.all()
     return render(request,
                       'market/vitrina.html',
                      {'items': items})