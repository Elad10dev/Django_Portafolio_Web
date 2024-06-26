from django.shortcuts import render

# Create your views here.
def Index(request):
    '''Esto es la pàgina principal'''
    return render(request, 'index.html')
